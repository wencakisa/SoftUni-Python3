FLASK_COVER_AREA = 1.76  # m^2


def main():
    wall_width = float(input())
    wall_height = float(input())

    wall_area = wall_width * wall_height
    flasks = 0

    while wall_area > 0:
        flasks += 1
        wall_area -= FLASK_COVER_AREA

    print(flasks)


if __name__ == '__main__':
    main()
