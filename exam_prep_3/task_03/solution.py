import sys
import csv
from math import pi


def main():
    try:
        rakia_liters_in_dm = float(input())  # 1l == 1dm^3

        if rakia_liters_in_dm <= 0:
            raise ValueError('Liters must be > 0!')

        containers_filename = input()
        containers = load_containers(containers_filename)

        suitable_containers = get_suitable_containers(containers, rakia_liters_in_dm)

        print(min(suitable_containers, key=lambda n: n[1])[0] if suitable_containers else 'NO SUITABLE CONTAINER')
        return 0
    except Exception:
        print('INVALID INPUT')
        return 1


def load_containers(containers_filename: str) -> list:
    result = []
    with open(containers_filename, encoding='utf-8') as f:
        for row in csv.reader(f):
            if row:
                name, radius, height = row
                radius = float(radius)
                height = float(height)

                result.append((name, radius, height))

    return result


def get_suitable_containers(containers: list, rakia_liters_in_dm: float) -> list:
    result = []
    for name, radius, height in containers:
        capacity_in_cm = pi * (radius ** 2) * height
        capacity_in_dm = capacity_in_cm / 1000

        if capacity_in_dm >= rakia_liters_in_dm:
            result.append((name, capacity_in_dm))

    return result

if __name__ == '__main__':
    sys.exit(main())
