import itertools
import sys
import logging


def main():
    data = sys.stdin.read().splitlines()
    ALICE, BOB = range(2)
    answer = ['Bob', 'Alice']
    for i in range(1, len(data), 2):
        N = int(data[i])
        pattern = map(int, data[i+1].split())
        logging.debug('PATTERN: %s' % pattern )
        
        j = len(pattern) - 1
        while pattern[j-1] > pattern[j]:
            j -= 1
        else:
            print answer[j%2]
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()