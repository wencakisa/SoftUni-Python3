from collections import Counter


def main():
    print(Counter(str(input()).strip()).most_common(1)[0][0])


if __name__ == '__main__':
    main()
