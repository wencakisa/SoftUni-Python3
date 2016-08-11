import sys


def main():
    try:
        words_file = input()
        word_to_search = input()

        with open(words_file, encoding='utf-8') as f:
            words = [word.strip() for word in f]

        anagrams = [
            word
            for word in words
            if sorted(word) == sorted(word_to_search) and
            word != word_to_search
        ]

        print('\n'.join(sorted(anagrams)) if anagrams else 'NO ANAGRAMS')

        return 0
    except Exception:
        print('INVALID INPUT')
        return 1

if __name__ == '__main__':
    sys.exit(main())
