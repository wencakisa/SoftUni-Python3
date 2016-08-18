import sys


def main():
    try:
        exchange_filename = input()
        amounts_filename = input()

        exchange_data = load_exchange_data(exchange_filename)
        for currency, amount in load_amounts_data(amounts_filename):
            if currency in exchange_data:
                amount_in_exchange_currency = amount / exchange_data[currency]
                print('{:.2f}'.format(amount_in_exchange_currency))
        return 0
    except Exception:
        print('INVALID INPUT')
        return 1


def load_exchange_data(exchange_filename: str) -> dict:
    result = {}
    with open(exchange_filename, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                exchange_currency, exchange_rate = line.split(' ')

                result[exchange_currency] = float(exchange_rate)

    return result


def load_amounts_data(amounts_filename: str):
    with open(amounts_filename, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                amount, currency, = line.split(' ')

                yield currency, float(amount)

if __name__ == '__main__':
    sys.exit(main())
