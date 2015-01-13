import math
import sys
import logging


def get_centroid(points):
    c_x = sum((x for x,y in points))/len(points)
    c_y = sum((y for x,y in points))/len(points)
    logging.debug('Centroid: %s' % ((c_x, c_y),))
    return (c_x, c_y)

def distance(p0, p1):
    return int(math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2))

def abs_distance(p0, p1):
    return max(abs(p0[0] - p1[0]), abs(p0[1]-p1[1]))

def main():
    data = sys.stdin.read().splitlines()
    points = []
    for d in data[1:]:
        if d == '':
            break
        x, y = d.split()
        points.append((int(x), int(y)))
    logging.debug('Points: %s' % points)
    
    centroid = get_centroid(points)
    
    central_point = min(points, key=lambda x: distance(centroid, x))
    logging.debug('Central Point: %s' % (central_point,))
    
    min_distance = sum((abs_distance(central_point, x) for x in points))
    logging.debug('Minimum sum of distances: %s' % (min_distance))
    print min_distance
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()