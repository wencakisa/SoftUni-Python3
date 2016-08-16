import sys


def main():
    try:
        words_filename = input()
        word_input = input()

        words = load_words(words_filename)
        anagrams = []
        for word in words:
            if sorted(word) == sorted(word_input) and word != word_input:
                anagrams.append(word)

        print('\n'.join(sorted(anagrams)) if anagrams else 'NO ANAGRAMS')
        return 0
    except Exception:
        print('INVALID INPUT')
        return 1


def load_words(words_filename: str):
    with open(words_filename) as f:
        return [line.strip() for line in f]

if __name__ == '__main__':
    sys.exit(main())
