from math import pi


def main():
    try:
        rakia_liters = float(input())  # dm^3
        containers_filename = str(input())

        if rakia_liters <= 0:
            raise ValueError('Invalid rakia liters: {}'.format(rakia_liters))

        containers = load_containers(containers_filename)

        print(get_min_suitable_container(rakia_liters, containers))
    except Exception:
        print('INVALID INPUT')


def load_containers(containers_filename: str) -> list:
    result = []

    with open(containers_filename, encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            if line:
                name, radius, height = line.split(',')
                result.append((name, float(radius), float(height)))

    return result


def get_min_suitable_container(rakia_liters: float, containers: list) -> str:
    result = []

    for name, radius, height in containers:
        capacity = pi * (radius ** 2) * height
        capacity /= 1000  # Convert from cm^3 to dm^3

        if capacity >= rakia_liters:
            result.append((name, capacity))

    return min(result, key=lambda c: c[1])[0] if result else 'NO SUITABLE CONTAINER'


if __name__ == '__main__':
    main()
