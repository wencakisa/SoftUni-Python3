def main():
    try:
        w = float(input())
        h = float(input())
        d = float(input())

        filename = str(input())

        box_dimensions = sorted((w, h, d))
        medic_data = load_data(input_filename=filename)

        fitting = get_fitting(box_dimensions, medic_data)

        print('\n'.join(fitting))
    except Exception:
        print('INVALID INPUT')


def load_data(input_filename):
    import csv

    with open(input_filename, encoding='utf-8') as f:
        return [(line[0], sorted([float(line[1]), float(line[2]), float(line[3])])) for line in csv.reader(f) if line]


def get_fitting(box_dimensions, medic_data):
    return [
        name
        for name, dimensions in medic_data
        if all(dimensions[dim_index] <= box_dimensions[dim_index] for dim_index in range(3))
    ]

if __name__ == '__main__':
    main()
