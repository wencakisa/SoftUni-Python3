import sys
import csv

TEMP_DIFFERENCE = 4.0


def main():
    try:
        input_filename = input()

        last_temp = None
        for dt, temp in load_temp_info(input_filename):
            if last_temp is None:
                last_temp = temp

            if temp - last_temp >= TEMP_DIFFERENCE:
                print(dt)

            last_temp = temp
        return 0
    except Exception:
        print('INVALID INPUT')
        return 1


def load_temp_info(input_filename: str):
    with open(input_filename) as f:
        for row in csv.reader(f):
            dt = row[0]
            temp = float(row[1])

            yield dt, temp

if __name__ == '__main__':
    sys.exit(main())
