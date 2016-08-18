import sys
import csv
from collections import defaultdict

import iso8601


def main():
    try:
        city_info_filename = str(input())

        city_info = load_city_info(city_info_filename)
        cities_with_missing_data = get_missing_data_cities(city_info)

        if cities_with_missing_data:
            for date, cities in sorted(cities_with_missing_data, key=lambda l: l[0]):
                print('{},{}'.format(date, ','.join(sorted(cities))))
        else:
            print('ALL DATA AVAILABLE')

        return 0
    except Exception:
        print('INVALID INPUT')
        return 1


def load_city_info(city_info_filename: str) -> defaultdict(set):
    result = defaultdict(set)

    with open(city_info_filename, encoding='utf-8') as f:
        for row in csv.reader(f):
            if row:
                date_str, city = row
                date = iso8601.parse_date(date_str).date()

                result[date].add(city)

    return result


def get_missing_data_cities(city_info: defaultdict(set)) -> list:
    all_cities = max(city_info.values())

    return [
        (date, all_cities - cities)
        for date, cities in city_info.items()
        if all_cities - cities
    ]

if __name__ == '__main__':
    sys.exit(main())
