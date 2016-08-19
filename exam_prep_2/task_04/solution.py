import sys
import csv

TEMP_DIFFERENCE = 4.0


def main():
    try:
        input_filename = input()

        previous_temp = None
        for current_dt, current_temp in load_temp_info(input_filename):
            if previous_temp is not None:
                if current_temp - previous_temp >= TEMP_DIFFERENCE:
                    print(current_dt)

            previous_temp = current_temp
        return 0
    except Exception:
        print('INVALID INPUT')
        return 1


def load_temp_info(input_filename: str) -> tuple:
    with open(input_filename, encoding='utf-8') as f:
        for row in csv.reader(f):
            dt, temp = row

            yield dt, float(temp)

if __name__ == '__main__':
    sys.exit(main())
