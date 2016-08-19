import sys


def main():
    try:
        words_filename = input()
        word_input = input()

        anagrams = []
        for word in load_words(words_filename):
            if sorted(word) == sorted(word_input) and word != word_input:
                anagrams.append(word)

        print('\n'.join(sorted(anagrams)) if anagrams else 'NO ANAGRAMS')
        return 0
    except Exception:
        print('INVALID INPUT')
        return 1


def load_words(words_filename: str) -> str:
    with open(words_filename, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                yield line

if __name__ == '__main__':
    sys.exit(main())
