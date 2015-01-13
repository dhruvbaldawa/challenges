import itertools
import sys
import logging


def main():
    data = sys.stdin.read().splitlines()
    numbers = map(int, data[1].split())
    combinations = {x for x in itertools.combinations(numbers, 3)
                    if x[0] < x[1] < x[2]}
    print len(combinations)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()