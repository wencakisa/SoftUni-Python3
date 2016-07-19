import re


def main():
    sentence = 'Python 3 can do so much, but I have to learn now.'
    index = 10

    print(slice_after_index(sentence, index))

    sentence_2 = 'This is soo difficult, I prefer playing WoW.'
    substring = 'soo'

    print(slice_after_substring(sentence_2, substring))


def slice_after_index(string: str, index: int) -> str:
    return string[:index] + '...'


def slice_after_substring(string: str, substring: str) -> str:
    return string[re.search(r'\b{}\b'.format(substring), string).span()[1]:].strip()

if __name__ == '__main__':
    main()
