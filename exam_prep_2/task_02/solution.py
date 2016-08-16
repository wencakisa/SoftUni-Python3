import sys
import string


def main():
    try:
        encoding_key = int(input())
        message_to_encode = str(input())

        print(encode(key=encoding_key, message=message_to_encode))
        return 0
    except Exception:
        print('INVALID INPUT')
        return 1


def encode(key: int, message: str) -> str:
    alphabet = string.ascii_uppercase
    encoding_alphabet = alphabet[key:] + alphabet[:key]

    return ''.join(encoding_alphabet[alphabet.find(letter)] if letter.isalpha() else letter for letter in message)

if __name__ == '__main__':
    sys.exit(main())
