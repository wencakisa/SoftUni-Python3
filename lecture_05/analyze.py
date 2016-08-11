import sys
import os

from lecture_05.sales import load_sales_data
from lecture_05.catalog import load_catalog_data
from lecture_05.analyzers import TotalsAnalyzer, AmountsByCategoryAnalyzer, AmountsByCityAnalyzer, AmountsByHourAnalyzer


def main():
    try:
        catalog_filename, sales_filename = parse_cmd_line_params()

        print('. . . Извличане на информация за продажби . . .')

        catalog = load_catalog_data(catalog_filename)
        sales_data_generator = load_sales_data(sales_filename)

        analyzers = [
            TotalsAnalyzer(),
            AmountsByCategoryAnalyzer(catalog),
            AmountsByCityAnalyzer(catalog),
            AmountsByHourAnalyzer(catalog)
        ]

        for sale in sales_data_generator:
            for analyzer in analyzers:
                analyzer.analyze_sale(sale)

        for analyzer in analyzers:
            analyzer.print_results()

        return 0
    except Exception as e:
        print('Error: {}'.format(str(e)))
        return 1


def parse_cmd_line_params() -> tuple:
    if len(sys.argv) < 3:
        print('Usage: {} <catalog.csv> <sales.csv>'.format(sys.argv[0]))
        sys.exit(2)

    catalog_filename, sales_filename = sys.argv[1:3]

    if not os.path.isfile(catalog_filename) or not os.access(catalog_filename, os.R_OK):
        raise ValueError('Invalid or inaccessible catalog file: {}'.format(catalog_filename))
    if not os.path.isfile(catalog_filename) or not os.access(catalog_filename, os.R_OK):
        raise ValueError('Invalid or inaccessible sales file: {}'.format(sales_filename))

    return catalog_filename, sales_filename

if __name__ == '__main__':
    sys.exit(main())
