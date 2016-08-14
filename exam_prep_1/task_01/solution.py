import sys
from collections import Counter


def main():
    try:
        print(Counter(input()).most_common(1)[0][0])
        return 0
    except Exception:
        print('INVALID INPUT')
        return 1

if __name__ == '__main__':
    sys.exit(main())
