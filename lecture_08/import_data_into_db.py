import sys
import os
import sqlite3

from lecture_08.sales import load_sales_data
from lecture_08.catalog import load_catalog_data
from lecture_08.db_utils import import_data


def main():
    try:
        catalog_filename, sales_filename, db_filename = parse_cmd_line_params()

        print('. . . Зареждане на информация за продажби . . .')

        catalog = load_catalog_data(catalog_filename)
        sales_data_generator = load_sales_data(sales_filename)

        with sqlite3.connect(db_filename, isolation_level=None) as connection:
            import_data(catalog, sales_data_generator, connection)

        return 0
    except Exception as e:
        print('Error: {}'.format(str(e)))
        return 1


def parse_cmd_line_params() -> tuple:
    if len(sys.argv) < 4:
        print('Usage: {} <catalog.csv> <sales.csv> <output.db>'.format(sys.argv[0]))
        sys.exit(2)

    catalog_filename, sales_filename, db_filename = sys.argv[1:4]

    if not os.path.isfile(catalog_filename) or not os.access(catalog_filename, os.R_OK):
        raise ValueError('Invalid or inaccessible catalog file: {}'.format(catalog_filename))
    if not os.path.isfile(catalog_filename) or not os.access(catalog_filename, os.R_OK):
        raise ValueError('Invalid or inaccessible sales file: {}'.format(sales_filename))
    if not os.path.isfile(db_filename) or not os.access(db_filename, os.R_OK):
        raise ValueError('Invalid or inaccessible database file: {}'.format(db_filename))

    return catalog_filename, sales_filename, db_filename

if __name__ == '__main__':
    sys.exit(main())
