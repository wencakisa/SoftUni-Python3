import sys
import csv


def main():
    try:
        item_id_name_input = input()
        input_filename = input()

        items = get_items_with_id(item_id_name_input, input_filename)
        items.sort(key=lambda l: l[1], reverse=True)

        print(items.pop()[0])
        return 0
    except Exception:
        print('INVALID INPUT')
        return 1


def get_items_with_id(item_id_name_input: str, input_filename: str):
    result = []

    with open(input_filename) as f:
        for row in csv.reader(f):
            item_id_name = row[0]
            item_city_name = row[2]
            item_price = float(row[4])

            if item_id_name == item_id_name_input:
                result.append((item_city_name, item_price))

    return result
if __name__ == '__main__':
    sys.exit(main())
