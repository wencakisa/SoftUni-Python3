import sys
import csv


def main():
    try:
        input_filename = input()

        total_time = 0
        with open(input_filename) as f:
            for row in csv.reader(f):
                km_from, km_to, speed_limit = tuple(map(int, row))
                total_kilometers = km_to - km_from + 1

                total_time += total_kilometers / speed_limit

        print('{:.2f}'.format(total_time))
        return 0
    except Exception as e:
        print('INVALID INPUT: {}'.format(e))
        return 1

if __name__ == '__main__':
    sys.exit(main())
