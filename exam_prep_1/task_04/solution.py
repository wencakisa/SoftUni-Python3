import sys


def main():
    try:
        exchange_filename = input()
        amounts_filename = input()

        exchange_data = load_exchange_data(exchange_filename)
        amounts_data = load_amounts_data(amounts_filename)

        for currency, amount in amounts_data:
            print('{:.2f}'.format(amount / exchange_data[currency]))

        return 0
    except Exception as e:
        print('INVALID INPUT: {}'.format(e))
        return 1


def load_exchange_data(exchange_filename):
    result = {}

    with open(exchange_filename, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                currency, exchange_rate = line.split(' ')
                result[currency] = float(exchange_rate)

    return result


def load_amounts_data(amounts_filename):
    result = []

    with open(amounts_filename, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                amount, currency = line.split(' ')
                result.append((currency, float(amount)))

    return result


if __name__ == '__main__':
    sys.exit(main())
