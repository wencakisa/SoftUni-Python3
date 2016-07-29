import sys

from lecture_05.utils import parse_cmd_line_params, load_csv_file
from lecture_05.catalog import load_catalog_data
from lecture_05.sales import load_sales_data, test_sales_data
from lecture_05.analyze_functions import get_summary, get_sales_by_category, get_sales_by_city, get_sales_by_timestamp
from lecture_05.print_functions import print_summary, print_sales_by_criteria


def main():
    try:
        catalog_filename, sales_filename = parse_cmd_line_params(sys.argv)

        print('. . . Извличане на информация за продажби . . .')

        catalog = load_catalog_data(load_csv_file(filename=catalog_filename))
        sales = load_sales_data(load_csv_file(filename=sales_filename))

        if test_sales_data(sales):
            sales_to_display = [
                ('Сума на продажби по категории', get_sales_by_category(catalog, sales)),
                ('Сума на продажби по градове', get_sales_by_city(sales)),
                ('Часове с най-голяма сума продажби', get_sales_by_timestamp(sales))
            ]

            print_summary(get_summary(sales))

            for criteria_title, sales_by_criteria in sales_to_display:
                print_sales_by_criteria(title=criteria_title, sales_to_display=sales_by_criteria)
                print('')

        return 0
    except Exception as e:
        print('Error: {}'.format(str(e)))
        return 1

if __name__ == '__main__':
    sys.exit(main())
