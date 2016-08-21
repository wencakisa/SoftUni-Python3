import sys

OPENING_BRACKET = '('
CLOSING_BRACKET = ')'


def main():
    try:
        brackets = input()

        if not brackets:
            raise ValueError('Empty string provided.')

        opening_brackets = len(brackets.split(OPENING_BRACKET))
        closing_brackets = len(brackets.split(CLOSING_BRACKET))

        first_opening_bracket_index = brackets.find(OPENING_BRACKET)
        first_closing_bracket_index = brackets.find(CLOSING_BRACKET)

        if opening_brackets == closing_brackets and first_opening_bracket_index <= first_closing_bracket_index:
            print('OK {}'.format(opening_brackets - 1))
        else:
            print('WRONG {}'.format(len(brackets)))

        return 0
    except Exception:
        print('INVALID INPUT')
        return 1

if __name__ == '__main__':
    sys.exit(main())
