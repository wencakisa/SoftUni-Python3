import sys
import csv

TEMP_DIFFERENCE = 4.0


def main():
    try:
        fridge_temp_filename = input()

        last_temp = None
        with open(fridge_temp_filename) as f:
            for dt, temp in load_temp_info(f):
                if last_temp is None:
                    last_temp = temp

                if temp - last_temp >= TEMP_DIFFERENCE:
                    print(dt)

                last_temp = temp
        return 0
    except Exception:
        print('INVALID INPUT')
        return 1


def load_temp_info(f):
    for row in csv.reader(f):
        yield (row[0], float(row[1]))

if __name__ == '__main__':
    sys.exit(main())
