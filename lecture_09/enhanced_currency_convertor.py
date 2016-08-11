import sys

import requests

API_URL = 'http://api.fixer.io/{date}?base={base_currency}'

EXCHANGE_RATES_KEY = 'rates'
ERROR_MSG_KEY = 'error'


def main():
    from_date = input('Въведете дата (yyyy-mm-dd): ')
    from_currency = input('Въведете валута: ')
    from_amount = float(input('Въведете сума: '))
    to_currency = input('Въведете валута, към която да се конвертира: ')

    print('\n. . . Извличане на валутни курсове . . .\n')

    api_url_formatted = API_URL.format(date=from_date, base_currency=to_currency)
    exchange_rates = get_exchange_rates(request_url=api_url_formatted)

    print('Равностойност в {}: {:.2f}'.format(
        to_currency,
        from_amount / get_conversion_rate(from_currency, exchange_rates)
    ))

    return 0


def get_exchange_rates(request_url: str) -> dict:
    resp = requests.get(request_url, timeout=5)
    resp_json = resp.json()

    try:
        return resp_json[EXCHANGE_RATES_KEY]
    except KeyError:
        print(resp_json[ERROR_MSG_KEY])
        sys.exit(2)


def get_conversion_rate(from_currency: str, exchange_rates: dict) -> float:
    try:
        return exchange_rates[from_currency]
    except KeyError:
        print('Няма информация за валута: {}'.format(from_currency))
        sys.exit(2)


if __name__ == '__main__':
    sys.exit(main())
