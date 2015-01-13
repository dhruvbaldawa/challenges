import itertools
import sys
import logging


def main():
    data = sys.stdin.read().splitlines()[1:]
    ratings = map(int, data)
    #candies = len(ratings)
    candies = 0
    #ratings.sort()
    high = 0
    for x in xrange(1, len(ratings)):
        prev = x - 1
        if ratings[x] > ratings[prev]:
            candies += high+1
            high += 1
        elif ratings[x] < ratings[prev]:
            candies += max(high-1, 0)
            high = max(high-1, 0)
        else:
            candies += 1
            high = 1
    
    print candies, candies+len(ratings)
                

    
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()