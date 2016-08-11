import sys
import csv

TEMP_DIFFERENCE = 4.0


def main():
    try:
        input_filename = input()

        last_temp = None
        for dt_str, temp in load_temperature_data(input_filename):
            if last_temp:
                if temp - last_temp > TEMP_DIFFERENCE:
                    print(dt_str)

            last_temp = temp

        return 0
    except Exception:
        print('INVALID INPUT')
        return 1


def load_temperature_data(input_filename: str):
    with open(input_filename, encoding='utf-8') as f:
        for row in csv.reader(f):
            yield (row[0], float(row[1]))


if __name__ == '__main__':
    sys.exit(main())
