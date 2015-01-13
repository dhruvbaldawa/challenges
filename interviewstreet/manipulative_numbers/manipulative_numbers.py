import itertools
import logging
import sys
import math
from collections import deque

xor = lambda x: x[0] ^ x[1]

def main():
    data = sys.stdin.read().splitlines()
    #data = open("input01.txt").read().splitlines()
    A = map(int, data[1].split())
    A = deque(A)
    logging.debug('A=%s' % A)
    K = 0

    pairs = [x for x in itertools.product(A, repeat=2)
        if x[0] != x[1]
        if x[0] < x[1]]
    # logging.debug("%s" % pairs)

    valid_filter = lambda x: sum(map(sum, x)) == 2*sum(A) # each element should be present twice
    valid_combinations = (
            x for x in itertools.combinations(pairs, len(A)) # get combination of length A.
                if valid_filter(x)
    )

    for B in valid_combinations:
        M_B = min(map(xor, B))
        if M_B > K:
            K = M_B

    k = int(math.log(K, 2))
    if k > 0:
        print k
    else:
        print '-1'


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()