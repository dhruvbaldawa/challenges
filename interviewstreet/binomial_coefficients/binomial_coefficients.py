import sys
import logging
from math import ceil, log
from collections import Counter
# REFERENCE:
# http://thales.math.uqam.ca/~rowland/talks/The_number_of_nonzero_binomial_coefficients_modulo_p%5Ealpha.pdf

# from http://code.activestate.com/recipes/577939-base-expansionconversion-algorithm-python/
mod = lambda n,m: n%m
def base_expansion(n, from_, to):
    i = len(n)
    base10 = sum([pow(from_,i-k-1)*n[k] for k in range(i)])
    j = int(ceil(log(base10 + 1,to)))
    baseExpanded = [mod(base10//pow(to,j-p),to) for p in range(1,j+1)]
    return baseExpanded


def main():
    data = sys.stdin.read().splitlines()[1:]
    for line in data:
        n, P = map(int, line.split())
        converted_base = base_expansion(map(int, str(n)), 10, P)
        #print converted_base
        d = Counter(converted_base)
        #print d
        ans = 1
        for key, value in d.iteritems():
            ans *= (key+1)**value
        print n + 1 - ans
        logging.debug('Done for n=%s, P=%s:' % (n, P))
        
        
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()