import csv
from collections import defaultdict

import iso8601


def main():
    try:
        city_temp_filename = str(input())

        city_data = load_city_data(city_temp_filename)
        cities_with_missing_data = get_cities_with_missing_data(city_data)

        if cities_with_missing_data:
            for date, cities in sorted(cities_with_missing_data, key=lambda t: t[0]):
                print('{},{}'.format(date, ','.join(sorted(cities))))
        else:
            print('ALL DATA AVAILABLE')

    except Exception:
        print('INVALID INPUT')


def load_city_data(city_temp_filename):
    result = defaultdict(set)

    with open(city_temp_filename, encoding='utf-8') as f:
        for line in csv.reader(f):
            if line:
                d_string, city, *_ = line

                d_string = iso8601.parse_date(d_string).date()
                result[d_string].add(city)

    return result


def get_cities_with_missing_data(city_data: defaultdict(list)) -> list:
    all_cities = max(city_data.values())

    return [
        (date, all_cities - cities)
        for date, cities in city_data.items()
        if all_cities - cities
    ]

if __name__ == '__main__':
    main()
