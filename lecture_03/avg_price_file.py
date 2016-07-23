import csv
import logging

logging.basicConfig(filename='error.log', level=logging.DEBUG)

EXPECTED_COLUMNS = 7


def main():
    input_filename = 'catalog_full.csv'
    input_data = load_data(input_filename)

    prices = [float(product_info[-1]) for product_info in input_data]
    average_price = get_average_price(prices)

    print('Average price: {:.2f}$'.format(average_price))


def load_data(input_filename: str) -> list:
    result = []

    with open(input_filename, encoding='utf-8') as f:
        for line_index, line in enumerate(csv.reader(f)):
            if len(line) == EXPECTED_COLUMNS:
                result.append(line)
            else:
                print('Invalid line detected, so it was ignored. Check error.log')
                logging.warning('Invalid line: {}'.format(line_index))

    return result


def get_average_price(prices: list) -> float:
    return sum(prices) / len(prices)

if __name__ == '__main__':
    main()
