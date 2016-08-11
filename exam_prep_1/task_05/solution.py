import sys
import csv


def main():
    try:
        input_item_id = input()
        input_filename = input()

        input_data = load_input_data(input_item_id, input_filename)

        print(min(input_data, key=lambda n: n[1])[0])

        return 0
    except Exception:
        print('INVALID INPUT')
        return 1


def load_input_data(input_item_id, input_filename):
    result = []

    with open(input_filename, encoding='utf-8') as f:
        for line in csv.reader(f):
            item_id = line[0]
            item_city = line[2]
            item_price = line[-1]

            if item_id == input_item_id:
                result.append((item_city, float(item_price)))

    return result

if __name__ == '__main__':
    sys.exit(main())
