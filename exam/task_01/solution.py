import sys


def main():
    try:
        input_data = input()

        failing_integer_index = get_failing_integer_index(input_data)
        print(failing_integer_index if failing_integer_index != -1 else 'SORTED')

        return 0
    except Exception:
        print('INVALID INPUT')
        return 1


def get_failing_integer_index(input_data: str) -> int:
    """
    Checks if the given data is a valid sorted integer sequence
    :param input_data: string, containing integers splitted by one or more spaces : "1   3  4   5 6    15  17"
    :return: if the sequence is not sorted -> return the value of the integer that fails the sequence
             if the sequence is sorted -> return -1
    """
    last_number = None
    for index, number in enumerate(list(map(int, input_data.split()))):
        if last_number is not None:
            if number < last_number:
                return index

        last_number = number

    return -1

if __name__ == '__main__':
    sys.exit(main())
