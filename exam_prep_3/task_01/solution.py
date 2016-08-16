import sys
from math import ceil

LOSS_PERCENT = 0.098
LOSS_MULTIPLIER = 1 + LOSS_PERCENT


def main():
    try:
        sheet_area = float(input())  # m^2
        box_height = float(input())  # m
        box_width = float(input())  # m
        box_depth = float(input())  # m

        box_surface_area = 2 * (
            box_height * box_width +
            box_width * box_depth +
            box_depth * box_height
        )

        box_surface_area *= LOSS_MULTIPLIER

        print(ceil(box_surface_area / sheet_area))
        return 0
    except Exception:
        print('INVALID INPUT')
        return 1

if __name__ == '__main__':
    sys.exit(main())
