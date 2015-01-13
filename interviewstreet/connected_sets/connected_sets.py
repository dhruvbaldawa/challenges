import itertools
import sys
import logging


def get_connected_sets(x=0, y=0, matrix):
    try:
        return matrix[x][y] +
            get_connected_sets(x+1, y, matrix) +\
            get_connected_sets(x, y+1, matrix) +\
            get_connected_sets(x+1, y+1)

def main():
    data = sys.stdin.read().splitlines()
    cases = int(data[0])
    start = 1
    for case in range(cases):
        size = int(data[start])

        lists = data[start+1:start+size]
        matrix = [map(int, x.split()) for x in lists]
        get_connected_sets(matrix=matrix)

        start = start+size+1


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
