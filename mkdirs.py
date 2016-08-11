import os
import sys

FILENAME = 'solution.py'
DIR_FORMAT = 'task_0{}'


def main():
    directory, tasks = parse_cmd_line_params()

    dir_full = os.path.abspath(directory)
    for i in range(1, tasks + 1):
        os.chdir(dir_full)

        current_dir = os.path.join(dir_full, DIR_FORMAT.format(i))

        os.mkdir(current_dir)
        os.chdir(current_dir)

        with open(FILENAME, mode='w'):
            pass


def parse_cmd_line_params() -> tuple:
    if len(sys.argv) < 3:
        print('Usage: {} <directory> <tasks>'.format(sys.argv[0]))
        sys.exit(1)

    directory, tasks = sys.argv[1:3]

    if not os.access(directory, os.W_OK) or not os.path.exists(directory):
        raise ValueError('Invalid or inaccessible directory: {}'.format(directory))

    if not tasks.isdigit():
        raise ValueError('Tasks count must be integer.')
    else:
        tasks = int(tasks)

    if tasks <= 0:
        raise ValueError('Invalid tasks count provided: {}'.format(tasks))

    return directory, tasks


if __name__ == '__main__':
    main()
