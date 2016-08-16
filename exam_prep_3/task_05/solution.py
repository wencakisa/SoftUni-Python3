import sys
import csv
from collections import defaultdict


def main():
    try:
        input_filename = input()

        input_data = load_input_data(input_filename)

        if not input_data:
            raise ValueError('Empty input file.')

        unique_sales = get_unique_sales(sales=input_data)
        if unique_sales:
            for city, item_ids in sorted(unique_sales.items(), key=lambda l: l[0]):
                print(','.join([city] + sorted(item_ids)))
        else:
            print('NO UNIQUE SALES')

        return 0
    except Exception:
        print('INVALID INPUT')
        return 1


def load_input_data(input_filename: str) -> defaultdict(set):
    result = defaultdict(set)

    with open(input_filename, encoding='utf-8') as f:
        for row in csv.reader(f):
            item_id = row[0]
            item_city = row[2]

            result[item_id].add(item_city)

    return result


def get_unique_sales(sales: defaultdict(set)) -> defaultdict(list):
    result = defaultdict(list)

    for item_id, cities in sales.items():
        if len(cities) == 1:
            result[cities.pop()].append(item_id)

    return result

if __name__ == '__main__':
    sys.exit(main())
