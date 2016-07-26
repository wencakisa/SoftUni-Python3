import sys
import glob
from os.path import expanduser


def main():
    if len(sys.argv) != 3:
        print('Usage: <script> <path_to_search_in> <file_to_search>')
        return 1

    path, filename = expanduser(sys.argv[1]), sys.argv[2]

    matching_files = glob.glob('{}/**/{}'.format(path, filename), recursive=True)

    print('\n'.join(matching_files) if matching_files else 'No matches found.')

if __name__ == '__main__':
    main()
