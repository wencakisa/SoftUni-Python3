import sys
import csv


def main():
    try:
        input_filename = input()

        total_time = 0
        for km_from, km_to, speed_limit in load_input_data(input_filename):
            total_kilometers = km_to - km_from + 1
            total_time += total_kilometers / speed_limit
    
        print('{:.2f}'.format(total_time))
        return 0
    except Exception:
        print('INVALID INPUT')
        return 1


def load_input_data(input_filename: str):
    with open(input_filename, encoding='utf-8') as f:
        for row in csv.reader(f):
            yield tuple(map(int, row))

if __name__ == '__main__':
    sys.exit(main())
