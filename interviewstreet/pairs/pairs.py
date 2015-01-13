import itertools
import sys
import logging


def main():
    data = sys.stdin.read().splitlines()
    n, k = data[0].split()
    n, k = int(n), int(k)

    numbers = map(int, data[1].split())
    numbers = sorted(numbers)
    logging.debug('Numbers: %s' % numbers)

    counter = 0
    for current_head in xrange(len(numbers)-1):
        compare_head = current_head + 1
        try:
            diff = numbers[compare_head] - numbers[current_head]
            while diff <= k:
                diff = numbers[compare_head] - numbers[current_head]
                if diff == k:
                    counter += 1
                compare_head += 1
        except:
            pass
            
    
    logging.debug('Counter: %s' % counter)
    print counter
        

    
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()