import sys
from ft_filter import ft_filter


def filterstring(string, min_length):
    '''
    Accept a string and a minimum length, and return an iterator that yields \
    only the characters in the string that have a length greater than \
    the minimum length.
    '''
    if not isinstance(string, str):
        print("AssertionError: the arguments are bad")
        sys.exit(1)

    return ft_filter(lambda x: len(x) > min_length, string.split())


def main(argv):
    '''
    Main function to handle input and call the filterstring function.
    '''
    if len(argv) != 3:
        print("AssertionError: the arguments are bad")
        sys.exit(1)

    string = argv[1]
    try:
        min_length = int(argv[2])
    except ValueError:
        print("AssertionError: the arguments are bad")
        sys.exit(1)

    result = filterstring(string, min_length)
    print(result)


if __name__ == "__main__":
    main(sys.argv)
