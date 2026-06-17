import sys


def odd_or_even(number: int) -> str:
    if number % 2 == 0:
        return "I'm Even"
    else:
        return "I'm Odd"


def error(message: str)-> None:
    print(f"AssertionError: {message}")
    sys.exit(1)


argv = sys.argv

if len(argv) < 2:
    sys.exit(1)
elif len(argv) > 2:
    error("more than one argument is provided")

try:
    number = int(argv[1])
except ValueError:
    error("argument is not an integer")

print(odd_or_even(number))
