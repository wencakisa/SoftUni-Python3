from math import sqrt


def main():
    try:
        a = float(input())
        b = float(input())
        c = float(input())

        p = (a + b + c) / 2

        area = sqrt(p * (p - a) * (p - b) * (p - c))

        print('{:.2f}'.format(area))
    except Exception:
        print('INVALID INPUT')

if __name__ == '__main__':
    main()
