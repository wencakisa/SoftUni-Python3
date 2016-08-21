import sys
import csv


def main():
    try:
        item_id = input()
        input_filename = input()

        items = load_sales_filtered(item_id, input_filename)
        print(min(items, key=lambda l: l[1])[0])
        return 0
    except Exception:
        print('INVALID INPUT')
        return 1


def load_sales_filtered(item_id: str, input_filename: str) -> list:
    result = []
    with open(input_filename, encoding='utf-8') as f:
        for row in filter(lambda r: r[0] == item_id, csv.reader(f)):
            city = row[2]
            price = float(row[-1])

            result.append((city, price))

    return result
if __name__ == '__main__':
    sys.exit(main())
