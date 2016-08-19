import sys
import csv


def main():
    try:
        box_w = float(input())
        box_h = float(input())
        box_d = float(input())
        input_filename = input()

        box_dimensions = sorted((box_w, box_h, box_d))

        for package_name, package_dims in load_packages(input_filename):
            if all(
                package_dims[i] <= box_dims[i]
                for i in range(len(box_dims))
            ):
                print(package_name)
        return 0
    except Exception:
        print('INVALID INPUT')
        return 1


def load_packages(input_filename: str) -> tuple:
    with open(input_filename, encoding='utf-8') as f:
        for line in csv.reader(f):
            name, w, h, d = line
            yield name, float(w), float(h), float(d)

if __name__ == '__main__':
    sys.exit(main())
