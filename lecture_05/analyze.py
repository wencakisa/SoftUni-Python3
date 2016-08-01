import sys
import os
import csv

from lecture_05.catalog import load_catalog_data
from lecture_05.sales import load_sales_data, test_sales_data
from lecture_05.analyze_functions import get_summary, get_sales_by_criteria
from lecture_05.print_functions import print_summary, print_sales_by_criteria


def main():
    try:
        catalog_filename, sales_filename = parse_cmd_line_params()

        print('. . . Извличане на информация за продажби . . .')

        catalog = load_catalog_data(load_csv_file(filename=catalog_filename))
        sales = load_sales_data(load_csv_file(filename=sales_filename))

        if test_sales_data(sales):
            print_summary(get_summary(sales))

            for criteria_title, sales_by_criteria in get_sales_by_criteria(catalog, sales):
                print_sales_by_criteria(title=criteria_title, sales_to_display=sales_by_criteria)
                print('')

        return 0
    except Exception as e:
        print('Error: {}'.format(str(e)))
        return 1


def parse_cmd_line_params() -> tuple:
    if len(sys.argv) < 3:
        raise ValueError('Usage: analyze.py <catalog.csv> <sales.csv>')

    catalog_filename, sales_filename = sys.argv[1:3]

    if not os.path.isfile(catalog_filename) or not os.access(catalog_filename, os.R_OK):
        raise ValueError('Invalid or inaccessible catalog file: {}'.format(catalog_filename))
    if not os.path.isfile(catalog_filename) or not os.access(catalog_filename, os.R_OK):
        raise ValueError('Invalid or inaccessible sales file: {}'.format(sales_filename))

    return catalog_filename, sales_filename


def load_csv_file(filename: str):
    with open(filename, mode='r', encoding='utf-8') as f:
        yield from csv.reader(f)

if __name__ == '__main__':
    sys.exit(main())
