#!/usr/bin/env python

import sys


def error(message):
    '''Prints an error message and exits the program.'''
    print(f"AssertionError: {message}")
    sys.exit(1)


def type_str_counter(av):
    '''
    Counts the number of characters, upper letters, lower letters, \
        punctuation marks, spaces, and digits in the input string.
    '''
    punctuation_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    total = len(av)
    upper = sum(1 for char in av if char.isupper())
    lower = sum(1 for char in av if char.islower())
    punctuation = sum(1 for char in av if char in punctuation_chars)
    spaces = sum(1 for char in av if char.isspace())
    digits = sum(1 for char in av if char.isdigit())

    print(f"The text contains {total} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main(argv):
    '''Main function to handle input and call the type_str_counter function.'''
    try:
        if len(argv) < 2:
            print("What is the text to count?")
            input_str = sys.stdin.readline()
            type_str_counter(input_str)
        elif len(argv) > 2:
            error("more than one argument is provided")
        else:
            type_str_counter(argv[1])

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main(sys.argv)
