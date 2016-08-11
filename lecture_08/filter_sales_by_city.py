import sys
import os
import sqlite3


def main():
    try:
        db_filename = parse_db_filename_param()

        city_to_search = input('Въведете име на град: ')

        with sqlite3.connect(db_filename, isolation_level=None) as connection:
            print_occurrences(connection, city_to_search)

        return 0
    except Exception as e:
        print('Error: {}'.format(e))
        return 1


def parse_db_filename_param():
    if len(sys.argv) < 2:
        print('Usage: {} <sales.db>'.format(sys.argv[0]))
        sys.exit(2)

    db_filename = sys.argv[1]

    if not os.path.isfile(db_filename) or not os.access(db_filename, os.R_OK):
        raise ValueError('Invalid or inaccessible database file: {}'.format(db_filename))

    return db_filename


def print_occurrences(connection: sqlite3.Connection, city_to_search: str):
    cursor = connection.cursor()

    cursor.execute('select * from sales where city_name=? order by price asc;', [city_to_search])
    occurrences = cursor.fetchall()

    if occurrences:
        print('\nПродажби в град {}:\n'.format(city_to_search))

        max_padding = max(len(item) for item in occurrences)

        for row_index, row in enumerate(occurrences, start=1):
            item_key = row[1]
            sale_timestamp = row[4]
            price = row[5]

            print('Артикул #{:<{}}{}\t\tдата/час: {}\t\tсума: {}€'.format(
                row_index, max_padding, item_key, sale_timestamp, price
            ))
    else:
        print('Няма данни за продажби в град {}.'.format(city_to_search))

if __name__ == '__main__':
    sys.exit(main())
