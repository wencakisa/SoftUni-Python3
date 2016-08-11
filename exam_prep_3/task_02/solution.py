STEP_DIRECTION_X_MAPPING = {
    'right': 1,
    'left': -1
}
STEP_DIRECTION_Y_MAPPING = {
    'up': 1,
    'down': -1
}


def main():
    try:
        steps_filename = str(input())

        steps = load_steps(steps_filename)

        if not steps:
            raise ValueError('Empty input file.')

        x, y = get_end_point_x_y(steps)

        print('X {:.3f}'.format(x))
        print('Y {:.3f}'.format(y))
    except Exception:
        print('INVALID INPUT')


def load_steps(steps_filename: str) -> list:
    result = []

    with open(steps_filename, encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            if line:
                items = line.split(' ')

                if len(items) != 2:
                    raise ValueError("Wrong number of items: {}.".format(items))

                direction, mapping = items
                result.append((direction, float(mapping)))

    return result


def get_end_point_x_y(steps: list) -> tuple:
    x_coord, y_coord = 0, 0

    for direction, mapping in steps:
        if direction in STEP_DIRECTION_X_MAPPING:
            x_coord += STEP_DIRECTION_X_MAPPING[direction] * mapping
        elif direction in STEP_DIRECTION_Y_MAPPING:
            y_coord += STEP_DIRECTION_Y_MAPPING[direction] * mapping
        else:
            raise ValueError('Invalid direction.')

    return x_coord, y_coord


if __name__ == '__main__':
    main()
