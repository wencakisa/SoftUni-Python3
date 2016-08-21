import sys


def main():
    try:
        words_filename = input()
        word_to_check = input()
        word_to_check_sorted = sorted(word_to_check)

        anagrams = []
        for word in load_words(words_filename):
            if word_to_check_sorted == sorted(word) and word_to_check != word:
                anagrams.append(word)

        print('\n'.join(sorted(anagrams)) if anagrams else 'NO ANAGRAMS')
        return 0
    except Exception:
        print('INVALID INPUT')
        return 1


def load_words(words_filename: str) -> str:
    with open(words_filename, encoding='utf-8') as f:
        for line in f:
            yield line.strip()

if __name__ == '__main__':
    sys.exit(main())
