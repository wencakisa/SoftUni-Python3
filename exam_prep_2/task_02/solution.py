import sys
import string


def main():
    try:
        encrypting_key = int(input())
        message_to_encrypt = str(input())

        print(encrypt(
            key=encrypting_key,
            message=message_to_encrypt)
        )
        return 0
    except Exception:
        print('INVALID INPUT')
        return 1


def encrypt(key: int, message: str) -> str:
    alphabet = string.ascii_uppercase
    encrypting_alphabet = alphabet[key:] + alphabet[:key]  # MAGIC!

    return ''.join(encrypting_alphabet[alphabet.find(letter)] if letter.isupper() else letter for letter in message)

if __name__ == '__main__':
    sys.exit(main())
