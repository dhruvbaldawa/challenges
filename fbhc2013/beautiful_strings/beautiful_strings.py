import sys
import logging
from collections import Counter
import string


def find_beautiful(line):
    line = filter(lambda x: x in string.letters, line)
    line = line.lower()
    char_frequency = Counter(line)
    replace_map = {}
    counter = 26
    for char, _ in char_frequency.most_common():
        replace_map[char] = counter
        counter -= 1

    ans = sum((replace_map[x] for x in line))
    return ans


def main():
    data = sys.stdin.read().splitlines()[1:]
    for i, line in enumerate(data):
        print "Case #%s: %s" % (i+1, find_beautiful(line))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()