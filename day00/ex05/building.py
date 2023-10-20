import sys


def main():
    if len(sys.argv) > 2:
        raise AssertionError('please provide one only string')
    punctuations = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    s = sys.argv[1] if len(sys.argv) == 2 else sys.stdin.read()
    print('The text contains', len(s), 'characters:')
    print(sum(1 for char in s if char.isupper()), 'upper letters')
    print(sum(1 for char in s if char.islower()), 'lower letters')
    print(sum(1 for char in s if char in punctuations), 'punctuation marks')
    print(sum(1 for char in s if char.isspace()), 'spaces')
    print(sum(1 for char in s if char.isdigit()), 'digits')


if __name__ == "__main__":
    main()
