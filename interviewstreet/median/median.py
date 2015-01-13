import itertools
import sys
import logging
import bisect

max_set = []
min_set = []
def remove_element(haystack, pin):
    i = bisect.bisect_left(haystack, pin)
    try:
        if haystack[i] == pin:
            del haystack[i]
            return True
        else:
            return False
    except:
        return False


def main():
    data = sys.stdin.read().splitlines()[1:]
    for line in data:
        operation, element = line.split()
        element = int(element)
        
        logging.debug(('%s, %s')%(operation, element)) 
        # flag for checking if element was found or not
        not_found = False
        
        if operation == 'a':
            if len(min_set) == 0:
                min_set.append(element)
            elif len(max_set) != 0 and element > max_set[0]:
                bisect.insort_left(max_set, element)
            else:
                bisect.insort_left(min_set, element)
        
        elif operation == 'r':
            if not remove_element(max_set, element):
                if not remove_element(min_set, element):
                    not_found = True
        
        # re-arranging the max-set and min-set
        if len(max_set) > len(min_set):
            min_set.append(max_set[0])
            del max_set[0]
        elif len(min_set) > len(max_set)+1:
            max_set.insert(0, min_set[-1])
            del min_set[-1]
        
        # calculating the median
        if not_found or (not max_set and not min_set):
            print 'Wrong!'
        elif len(max_set) < len(min_set):
            print min_set[-1]
        elif len(max_set) > len(min_set):
            print max_set[0]
        elif len(max_set) == len(min_set):
            median = (max_set[0] + min_set[-1])/2.
            print median if int(median) != median else int(median)
         
        
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()