import sys
import logging


def process(str_):
    lstr = list(str_)
    i = len(lstr) - 2
    # find highest i such that s[i] < s[i+1]
    while i >= 0:
        if lstr[i] < lstr[i+1]:
            break
        i -= 1

    if i == -1:
        print 'no answer'
        return

    # find highest j > i such that s[j] > s[i]
    j = len(lstr) - 1
    while j > i:
        if lstr[j] > lstr[i]:
            break
        j -= 1

    lstr[j], lstr[i] = lstr[i], lstr[j]
    print ''.join(lstr[:i+1] + list(reversed(lstr[i+1:])))


def main():
    data = sys.stdin.read().splitlines()[1:]

    for string_ in data:
        process(string_)
        # for x in itertools.permutations(string_):
        #     if ''.join(x) > string_:
        #         print(''.join(x))
        #         break
        #     else:
        #         print '>>', ''.join(x)
        # else:
        #     print('no answer')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
