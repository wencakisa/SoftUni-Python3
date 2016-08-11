import sys
from collections import OrderedDict
from datetime import datetime

import requests

APP_ID = '965acdac1ae64cf06761bb563ad34d96'
API_URL = 'http://api.openweathermap.org/data/2.5/weather'
STATUS_CODE_OK = 200

KELVIN_TO_CELSIUS_SUBTRACT = 273.15


def main():
    city = input('Въведете град: ')

    print('\n. . . Извличане на метеорологична информация за град {} . . .\n'.format(city))

    params = OrderedDict([('appid', APP_ID), ('q', city)])
    resp = requests.get(API_URL, params=params, timeout=5)

    resp_json = resp.json()

    if resp_json['cod'] != STATUS_CODE_OK:
        print('Няма метеорологична информация за град {}'.format(city))
        return 2

    main_info = resp_json['main']
    wind_info = resp_json['wind']
    dt_timestamp = resp_json['dt']

    print('''Информация към: {dt}
Температура: {temperature:.1f}°C
Налягане: {pressure:.2f}hPa
Влажност: {humidity}%
Вятър: {wind_speed:.2f} м/с
'''.format(
        dt=datetime.fromtimestamp(dt_timestamp),
        temperature=main_info['temp'] - KELVIN_TO_CELSIUS_SUBTRACT,
        pressure=main_info['pressure'],
        humidity=main_info['humidity'],
        wind_speed=wind_info['speed']
    ))

    return 0

if __name__ == '__main__':
    sys.exit(main())
