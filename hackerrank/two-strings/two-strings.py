import sys
import logging


def main():
    data = sys.stdin.read().splitlines()[1:]
    groups = zip(data[::2], data[1::2])
    # print groups

    for x, y in groups:
        s = set(y)
        for char in x:
            if char in s:
                print('YES')
                break
        else:
            print('NO')

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
