import sys
from datetime import datetime

import requests
import pytz

APP_ID = '965acdac1ae64cf06761bb563ad34d96'
API_URL = 'http://api.openweathermap.org/data/2.5/weather'
STATUS_CODE_OK = 200

KELVIN_TO_CELSIUS_SUBTRACT = 273.15


def main():
    city = input('Въведете град: ')

    print('\n. . . Извличане на метеорологична информация за град {} . . .\n'.format(city))

    response = requests.get(API_URL, params={'q': city, 'appid': APP_ID}, timeout=20)
    response_json = response.json()

    if response_json['cod'] != STATUS_CODE_OK:
        print(response_json['message'])
        return 2

    main_info = response_json['main']
    wind_info = response_json['wind']
    dt_timestamp = response_json['dt']

    print('''Информация към: {dt}
Температура: {temperature:.1f}°C
Налягане: {pressure:.2f}hPa
Влажност: {humidity}%
Вятър: {wind_speed:.2f} м/с
'''.format(
        dt=datetime.fromtimestamp(dt_timestamp, tz=pytz.utc).strftime('%d-%m-%Y %H:%m'),
        temperature=main_info['temp'] - KELVIN_TO_CELSIUS_SUBTRACT,
        pressure=main_info['pressure'],
        humidity=main_info['humidity'],
        wind_speed=wind_info['speed']
    ))

    return 0

if __name__ == '__main__':
    sys.exit(main())
