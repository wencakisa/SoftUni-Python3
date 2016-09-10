import sys

TELEPHONE_KEYBOARD = {
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z'],
    0: [' ']
}


def main():
    try:
        text = input()

        if not text.strip():
            raise ValueError('Empty string provided.')

        for letter in text:
            for number, letters in TELEPHONE_KEYBOARD.items():
                if letter in letters:
                    print(str(number) * (letters.index(letter) + 1), end='')

        return 0
    except Exception:
        print('INVALID INPUT')
        return 1

if __name__ == '__main__':
    sys.exit(main())
