import sys
import csv


def main():
    try:
        item_id = input()
        input_filename = input()

        items = load_sales_filtered(item_id, input_filename)
        items.sort(key=lambda l: l[1], reverse=True)
        print(items[0][0])
        return 0
    except Exception:
        print('INVALID INPUT')
        return 1


def load_sales_filtered(item_id: str, input_filename: str) -> list:
    result = []
    with open(input_filename, encoding='utf-8') as f:
        for row in filter(lambda r: r[0] == item_id, csv.reader(f)):
            item_city_name = row[2]
            item_price = float(row[-1])

            result.append((item_city_name, item_price))

    return result
if __name__ == '__main__':
    sys.exit(main())
