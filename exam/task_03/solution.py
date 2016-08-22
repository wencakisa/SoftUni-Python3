import sys

OPENING_BRACKET = '('
CLOSING_BRACKET = ')'


def main():
    try:
        brackets = input()

        if not brackets:
            raise ValueError('Empty string provided.')

        opening_brackets_count = len(brackets.split(OPENING_BRACKET))
        closing_brackets_count = len(brackets.split(CLOSING_BRACKET))

        starting_brackets_index_difference = brackets.find(OPENING_BRACKET) - brackets.find(CLOSING_BRACKET)
        bracket_pairs = opening_brackets_count - 1

        if opening_brackets_count == closing_brackets_count and starting_brackets_index_difference >= 0:
            print('OK {}'.format(bracket_pairs))
        else:
            print('WRONG {}'.format(len(brackets)))

        return 0
    except Exception:
        print('INVALID INPUT')
        return 1

if __name__ == '__main__':
    sys.exit(main())
