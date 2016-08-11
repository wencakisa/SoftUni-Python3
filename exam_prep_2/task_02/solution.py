import string


def main():
    try:
        cipher_key = int(input())
        text_to_encode = input()

        print(encode(cipher_key, text_to_encode))
    except Exception:
        print('INVALID INPUT')


def encode(cipher_key: int, text_to_encode: str):
    alphabet = string.ascii_uppercase
    cipher = alphabet[cipher_key:] + alphabet[:cipher_key]

    return ''.join([symbol if not symbol.isalpha() else cipher[alphabet.find(symbol)] for symbol in text_to_encode])


if __name__ == '__main__':
    main()
