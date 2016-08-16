FLASK_AREA = 1.76  # m^2


def main():
    wall_width = float(input())
    wall_height = float(input())

    wall_area = wall_width * wall_height
    flasks_count = 0

    while wall_area >= 0:
        wall_area -= FLASK_AREA
        flasks_count += 1

    print(flasks_count)

if __name__ == '__main__':
    main()