import sys
import csv


def main():
    try:
        input_filename = input()
        input_data = load_input_data(input_filename)

        if not input_data:
            raise ValueError('Empty input file provided.')

        percentage = float(input())

        if percentage <= 0:
            raise ValueError('Negative percentages are not supported.')

        percentage_raise_data = get_percentage_raise_data(input_data, percentage)

        if percentage_raise_data:
            for date, percentage_raise in percentage_raise_data:
                print('{} {:.2f}'.format(date, percentage_raise))
        else:
            print('NO DRASTIC CHANGES; RECORDS COUNT: {}'.format(len(input_data)))

        return 0
    except Exception:
        print('INVALID INPUT')
        return 1


def load_input_data(input_filename: str) -> list:
    """
    Loads the data from the file in list from tuples
    :param input_filename:
    :return: list from tuples: (date, price) : (2016-08-21, 1553.43)
    """
    result = []

    with open(input_filename, encoding='utf-8') as f:
        for row in csv.reader(f):
            date, price = row

            result.append((date, float(price)))

    return result


def get_percentage_raise_data(input_data: list, percentage: float) -> list:
    """
    Checks whether prices percentage raise is above the given :param percentage
    :param input_data: list, containing tuples with (date, price) : (2016-08-21, 1553.43)
    :param percentage: the percentage rate to check
    :return: list from tuples: (date, percentage_raise) : (2016-08-21, 14.83)
    """
    result = []
    last_price = None

    for date, price in input_data:
        if last_price is not None:
            percentage_raise = (100 * price / last_price) - 100

            if percentage_raise >= percentage:
                result.append((date, percentage_raise))

        last_price = price

    return result

if __name__ == '__main__':
    sys.exit(main())
