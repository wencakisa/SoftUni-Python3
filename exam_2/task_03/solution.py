import sys
import csv
from collections import defaultdict

EXPECTED_COLUMNS_COUNT = 4
MEDAL_TYPE_COLUMN = 2
COUNTRY_COLUMN = 3

MEDALS_POINTS = {
    'gold': 7,
    'silver': 3,
    'bronze': 1
}


def main():
    try:
        input_filename = input()

        countries_points = defaultdict(int)
        for medal_type, country in load_input_data(input_filename):
            countries_points[country] += MEDALS_POINTS[medal_type]

        if not countries_points:
            raise ValueError('Empty input file provided.')

        for country, points in sorted(countries_points.items(), key=lambda kv: (kv[1], kv[0]), reverse=True):
            print(country)

        return 0
    except Exception:
        print('INVALID INPUT')
        return 1


def load_input_data(input_filename: str):
    with open(input_filename, encoding='utf-8') as f:
        for row in csv.reader(f):
            if len(row) != EXPECTED_COLUMNS_COUNT:
                raise ValueError('Wrong number of items: {}'.format(len(row)))

            yield row[MEDAL_TYPE_COLUMN], row[COUNTRY_COLUMN]


if __name__ == '__main__':
    sys.exit(main())
