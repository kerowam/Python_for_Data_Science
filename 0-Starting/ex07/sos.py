import sys


def morse_translate(text: str) -> str:
    '''Translate a given text into Morse code.'''
    morse_code = {
        ' ': '/', 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
        'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...',
        'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..'
    }
    return ''.join(morse_code.get(char.upper(), '') for char in text)


def main(argv: list[str]) -> None:
    '''Main function to handle input and call the morse_translate function.'''
    if len(argv) != 2:
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    try:
        text = argv[1]
        for char in text:
            if char.upper() not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ ":
                print("AssertionError: the arguments are bad")
                sys.exit(1)
        result = morse_translate(text)
        print(result)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv)
