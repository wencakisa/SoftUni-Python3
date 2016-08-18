import sys
import csv


def main():
    try:
        box_w = float(input())
        box_h = float(input())
        box_d = float(input())
        input_filename = input()

        box_dimensions = sorted((box_w, box_h, box_d))

        for package_name, package_dimensions in load_packages(input_filename):
            if package_fits_in_box(package_dimensions, box_dimensions):
                print(package_name)
        return 0
    except Exception:
        print('INVALID INPUT')
        return 1


def load_packages(input_filename: str):
    with open(input_filename, encoding='utf-8') as f:
        for line in csv.reader(f):
            name, *dimensions = line
            yield name, sorted(map(float, dimensions))


def package_fits_in_box(package_dimensions: list, box_dimensions: list) -> bool:
    return all(package_dimensions[dim_index] <= box_dimensions[dim_index] for dim_index in range(len(box_dimensions)))

if __name__ == '__main__':
    sys.exit(main())
