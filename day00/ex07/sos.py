import sys


sys.tracebacklimit = 0


def main():
    if len(sys.argv) != 2:
        raise AssertionError("Usage: python sos.py <input>")

    dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', ' ': '/'
    }

    input = sys.argv[1].upper()

    if not all(c in dict for c in input):
        raise AssertionError('the arguments are bad')

    output = ' '.join(dict[c] for c in input)

    print(output)


if __name__ == "__main__":
    main()
