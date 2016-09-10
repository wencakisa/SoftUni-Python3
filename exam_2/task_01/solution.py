import sys

PLURAL_WORD_ENDINGS_ES = ['o', 'ch', 's', 'sh', 'x', 'z']


def main():
    try:
        word = input()

        if not word.strip():
            raise ValueError('Empty string provided.')

        if any(word.endswith(ending) for ending in PLURAL_WORD_ENDINGS_ES):
            word += 'es'
        elif word.endswith('y'):
            word = word[:-1] + 'ies'
        else:
            word += 's'

        print(word)

        return 0
    except Exception:
        print('INVALID INPUT')
        return 1

if __name__ == '__main__':
    sys.exit(main())
