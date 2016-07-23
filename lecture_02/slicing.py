import re


def main():
    sentence = 'Python 3 can do so much, but I have to learn now.'
    index = 13
    substring = 'can'
    print(slice_after_index(sentence, index))

    print(slice_after_substring(sentence, substring))


def slice_after_index(string: str, index: int) -> str:
    return string[:index] + '...'


def slice_after_substring(string: str, substring: str) -> str:
    match = re.search(r'\b{}\b'.format(substring), string)

    return string[match.span()[1]:] if match else string

if __name__ == '__main__':
    main()
