import sys
import csv

ID_COLUMN = 0
X_COLUMN = 1
Y_COLUMN = 2


def main():
    try:
        input_filename = input()
        distance_difference = float(input())

        coordinates_data = load_coordinates_data(input_filename)

        if not coordinates_data:
            raise ValueError('Empty input file provided.')

        close_points = get_close_points_ids(coordinates_data, distance_difference)

        if close_points:
            print('\n'.join(close_points))
        else:
            print('NO CLOSE POINTS FOUND; RECORDS COUNT: {}'.format(len(coordinates_data)))

        return 0
    except Exception:
        print('INVALID INPUT')
        return 1


def load_coordinates_data(input_filename: str) -> list:
    result = []

    with open(input_filename, encoding='utf-8') as f:
        for row in csv.reader(f):
            result.append(
                (row[ID_COLUMN], float(row[X_COLUMN]), float(row[Y_COLUMN]))
            )

    return result


def get_close_points_ids(coordinates_data: list, distance_difference: float) -> list:
    result = []

    for previous_point, current_point in zip(coordinates_data, coordinates_data[1:]):
        _, previous_point_x, previous_point_y = previous_point
        current_point_id, current_point_x, current_point_y = current_point

        points_x_difference = abs(current_point_x - previous_point_x)
        points_y_difference = abs(current_point_y - previous_point_y)

        if points_x_difference <= distance_difference and points_y_difference <= distance_difference:
            result.append(current_point_id)

    return result


if __name__ == '__main__':
    sys.exit(main())
