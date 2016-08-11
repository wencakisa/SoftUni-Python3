import sys

import requests

TO_CURRENCY = 'BGN'
API_URL = 'http://api.fixer.io/latest?base={}'.format(TO_CURRENCY)

EXCHANGE_RATES_KEY = 'rates'


def main():
    from_currency = input('Въведете валута: ')
    from_amount = float(input('Въведете сума: '))

    print('\n. . . Извличане на валутни курсове . . .\n')

    resp = requests.get(API_URL)
    resp_json = resp.json()

    exchange_rates = resp_json[EXCHANGE_RATES_KEY]

    try:
        exchange_rate = exchange_rates[from_currency]
    except KeyError:
        print('Няма информация за валута: {}'.format(from_currency))
        return 2

    print('Равностойност в {}: {:.2f}'.format(TO_CURRENCY, from_amount / exchange_rate))

    return 0

if __name__ == '__main__':
    sys.exit(main())
