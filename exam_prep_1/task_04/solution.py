def main():
    exchange_filename = input()
    amounts_filename = input()

    exchange_data = load_exchange_data(exchange_filename)
    amounts_data = load_amounts_data(amounts_filename)

    for currency, amount in amounts_data:
        if currency in exchange_data:
            print('{:.2f}'.format(amount / exchange_data[currency]))


def load_exchange_data(exchange_filename):
    result = {}

    with open(exchange_filename) as f:
        for line in f:
            line = line.strip().split(' ')
            result[line[0]] = float(line[1])

    return result


def load_amounts_data(amounts_filename):
    result = []

    with open(amounts_filename) as f:
        for line in f:
            line = line.strip().split(' ')
            result.append((line[1], float(line[0])))

    return result

if __name__ == '__main__':
    main()
