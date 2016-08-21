import sys
import math

FLASK_AREA = 1.76


def main():
    try:
        wall_width = float(input())
        wall_height = float(input())
        wall_area = wall_width * wall_height

        print(math.ceil(wall_area / FLASK_AREA))
        return 0
    except Exception:
        print('INVALID INPUT')
        return 1

if __name__ == '__main__':
    sys.exit(main())
