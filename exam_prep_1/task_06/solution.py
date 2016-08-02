import csv


def main():
    filename = input()

    with open(filename) as f:
        result = [
            ((int(line[1]) - int(line[0]) + 1) / int(line[2]))
            for line in csv.reader(f)
        ]

    print('{:.2f}'.format(sum(result)))

if __name__ == '__main__':
    main()
