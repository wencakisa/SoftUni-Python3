import csv
from collections import defaultdict


def main():
    try:
        sales_filename = input()

        sales_data = load_sales_data(sales_filename)

        if not sales_data:
            raise ValueError('Empty input file.')

        unique_sales = get_unique_sales(sales_data)

        if unique_sales:
            for city, product_ids in sorted(unique_sales.items(), key=lambda i: i[0]):
                print('{},{}'.format(city, ','.join(sorted(product_ids))))
        else:
            print('NO UNIQUE SALES')
    except Exception:
        print('INVALID INPUT')


def load_sales_data(sales_filename):
    result = defaultdict(set)

    with open(sales_filename, encoding='utf-8') as f:
        for line in csv.reader(f):
            result[line[0]].add(line[2])

    return result


def get_unique_sales(sales_data):
    result = defaultdict(list)

    for product_id, cities in sales_data.items():
        if len(cities) == 1:
            result[cities.pop()].append(product_id)

    return result

if __name__ == '__main__':
    main()
