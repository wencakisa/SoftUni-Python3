import sys


def main():
    try:
        exchange_filename = input()
        amounts_filename = input()

        with open(exchange_filename, encoding='utf-8') as ex_f:
            exchange_data = load_exchange_data(exchange_file=ex_f)

            with open(amounts_filename, encoding='utf-8') as am_f:
                for currency, amount in load_amounts_data(amounts_file=am_f):
                    if currency in exchange_data:
                        amount_in_exchange_currency = amount / exchange_data[currency]
                        print('{:.2f}'.format(amount_in_exchange_currency))
        return 0
    except Exception:
        print('INVALID INPUT')
        return 1


def load_exchange_data(exchange_file):
    result = {}

    for line in exchange_file:
        line = line.strip()
        if line:
            exchange_currency, exchange_rate, *_ = line.split(' ')

            result[exchange_currency] = float(exchange_rate)

    return result


def load_amounts_data(amounts_file):
    for line in amounts_file:
        line = line.strip()
        if line:
            amount, currency, *_ = line.split(' ')
            yield (currency, float(amount))

if __name__ == '__main__':
    sys.exit(main())
