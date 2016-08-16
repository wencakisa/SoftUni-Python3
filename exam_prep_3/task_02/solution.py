import sys

STEP_DIRECTION_X_MAPPING = {
    'left': -1,
    'right': 1
}
STEP_DIRECTION_Y_MAPPING = {
    'down': -1,
    'up': 1
}


def main():
    try:
        input_filename = input()

        with open(input_filename) as f:
            steps_x_y = list(load_steps_as_x_y(f))

            if steps_x_y:
                print('X {:.3f}'.format(sum(i[0] for i in steps_x_y)))
                print('Y {:.3f}'.format(sum(i[1] for i in steps_x_y)))
            else:
                raise ValueError('Empty input file: {}'.format(input_filename))
        return 0
    except Exception:
        print('INVALID INPUT')
        return 1


def load_steps_as_x_y(f):
    for line in f:
        line = line.strip()
        if line:
            items = line.split(' ')
            if len(items) != 2:
                raise ValueError('Wrongs number of items: {}'.format(len(items)))

            direction, step_length = items
            step_length = float(step_length)

            if direction in STEP_DIRECTION_X_MAPPING:
                yield (step_length * STEP_DIRECTION_X_MAPPING[direction]), 0
            elif direction in STEP_DIRECTION_Y_MAPPING:
                yield 0, (step_length * STEP_DIRECTION_Y_MAPPING[direction])
            else:
                raise ValueError('Invalid direction: {}'.format(direction))

if __name__ == '__main__':
    sys.exit(main())
