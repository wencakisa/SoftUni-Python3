import math

LOSS_PERCENT = 0.098
LOSS_MULTIPLIER = 1 + LOSS_PERCENT


def main():
    try:
        paper_area = float(input())  # m^2
        box_height = float(input())  # m
        box_width = float(input())  # m
        box_depth = float(input())  # m

        box_surface_area = 2 * (
            box_height * box_width +
            box_width * box_depth +
            box_height * box_depth
        )

        box_surface_area *= LOSS_MULTIPLIER

        print(math.ceil(box_surface_area / paper_area))
    except Exception:
        print('INVALID INPUT')


if __name__ == '__main__':
    main()
