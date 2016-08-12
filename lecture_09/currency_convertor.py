import sys

import requests

DEFAULT_BASE_CURRENCY = 'BGN'
URL_API_LATEST = 'http://api.fixer.io/latest'
STATUS_CODE_OK = 200


def main():
    currency = input('Въведете валута: ')
    currency = currency.upper()

    amount_str = input('Въведете сума: ')
    try:
        amount = float(amount_str)
        if amount < 0:
            print('Поддържат се само суми >= 0!')
            return 1
    except ValueError:
        print('Невалидна стойност: {}'.format(amount_str))
        return 2

    base_currency = input('Въведете валута, към която да се преизчисли сумата [{}]: '.format(DEFAULT_BASE_CURRENCY))
    base_currency = base_currency.upper()

    if not base_currency:
        base_currency = DEFAULT_BASE_CURRENCY

    print('\n. . . Извличане на валутни курсове . . .\n')

    rates = get_exchange_rates(base_currency)

    if rates is None:
        print('Обменните курсове не могат да бъдат заредени! '
              'Моля, обърнете се към системния администратор.')
        return 2

    amount_in_base_currency = calculate_rate_in_base_currency(rates, currency, amount)

    if amount_in_base_currency is not None:
        print('Равностойност в {}: {:.2f}'.format(base_currency, amount_in_base_currency))
        return 0
    else:
        print('Няма информация за валута: {}'.format(currency))
        return 2


def calculate_rate_in_base_currency(rates: dict, currency: str, amount_in_currency: float) -> float:
    try:
        return amount_in_currency / rates[currency]
    except KeyError:
        return None


def get_exchange_rates(base_currency: str, api_url: str=URL_API_LATEST) -> dict:
    try:
        response = requests.get(api_url, params={'base': base_currency}, timeout=20)

        if response.status_code == STATUS_CODE_OK:
            exchange_rates = response.json()
            return exchange_rates.get('rates', {})
        else:
            print('Error from server. ({})'.format(response.status_code))
    except Exception as e:
        print('Error from server!!! ', str(e))

    return None

if __name__ == '__main__':
    sys.exit(main())
