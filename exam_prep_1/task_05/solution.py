import sys
import csv


def main():
    try:
        item_id = input()
        input_filename = input()

        items = list(filter(lambda sale: sale[0] == item_id, load_sales(input_filename)))
        items.sort(key=lambda l: l[2], reverse=True)
        print(items.pop()[1])
        return 0
    except Exception:
        print('INVALID INPUT')
        return 1


def load_sales(input_filename: str) -> list:
    result = []
    with open(input_filename, encoding='utf-8') as f:
        for row in csv.reader(f):
            item_id = row[0]
            item_city_name = row[2]
            item_price = float(row[-1])

            result.append(
                (item_id, item_city_name, item_price)
            )

    return result
if __name__ == '__main__':
    sys.exit(main())
