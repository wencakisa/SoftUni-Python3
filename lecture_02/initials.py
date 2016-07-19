def main():
    names = [
        'Венцислав Ташев',
        'John Lawrence Smith',
        'проф. Кирил Господинов',
        'Guido van Rossum',
        'Werher von Braun'
    ]

    for name in names:
        print('{}: {}'.format(name, get_initials(name)))


def get_initials(full_name: str) -> str:
    return '.'.join([
        name[0]
        for name in full_name.split(' ')
        if name[0].isupper()
    ])

if __name__ == '__main__':
    main()
