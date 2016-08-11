import sys


def main():
    try:
        w = float(input())
        h = float(input())
        d = float(input())
        input_filename = input()

        print('\n'.join(get_fitting(box_dimensions=sorted((w, h, d)), input_data=load_input_data(input_filename))))

        return 0
    except Exception:
        print('INVALID INPUT')
        return 1


def load_input_data(input_filename):
    result = []

    with open(input_filename, encoding='utf-8') as f:
        for line in f:
            if line.strip():
                name, *dimensions = line.split(',')

                result.append((name, sorted(map(float, dimensions))))

    return result


def get_fitting(box_dimensions, input_data):
    return [
        name for name, dimensions in input_data
        if all(dimensions[dim_index] <= box_dimensions[dim_index] for dim_index in range(3))
    ]


if __name__ == '__main__':
    sys.exit(main())
