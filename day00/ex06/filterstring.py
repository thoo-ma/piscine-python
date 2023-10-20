from ft_filter import ft_filter
import sys


sys.tracebacklimit = 0


def main():
    if len(sys.argv) != 3:
        raise AssertionError('wrong number of arguments')

    try:
        int(sys.argv[2])
    except ValueError:
        raise AssertionError('second arg should be a number') from None

    words = str(sys.argv[1]).split()
    n = int(sys.argv[2])

    print(ft_filter(lambda w: len(w) > n, words))


if __name__ == "__main__":
    main()
