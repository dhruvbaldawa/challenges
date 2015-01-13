import itertools
import sys
import logging
import math
from collections import defaultdict

#REFERENCE: http://stackoverflow.com/questions/9018614/algorithm-to-find-lucky-numbers
MAX_LENGTH = 18 # 10**18
MAX_SUM = 9 * MAX_LENGTH # 9 * 18
MAX_SUM_SQUARE = (9**2) * MAX_LENGTH # 9**2 * 18

def enumerate_primes(n): 
    if n == 2: return [2]
    elif n < 2: return []
    s = range(3,n+1,2)
    nroot = math.sqrt(n)
    half=(n+1)/2 - 1
    i = 0
    m = 3
    while m <= nroot:
        if s[i]:
            j = (m*m-3)/2
            s[j] = 0
            while j < half:
                s[j] = 0
                j += m
        i = i + 1
        m=2 * i + 3
    return [2] + [x for x in s if x]

# dict with tuple (i, j, k) as key.
# it stores an int which is the number of numbers with length i, sum of digits j
# and sum of square of digits k
dynamic_table = defaultdict(int)
primes = enumerate_primes(MAX_SUM_SQUARE)

def generate_dynamic_table():    
    dynamic_table[(0, 0, 0)] = 1
    for i in range(MAX_LENGTH):
        for j in range(9 * i+1):
            for k in range(9 * 9 * i+1):
                for l in range(10):
                    dynamic_table[(i+1, j+l, k+l*l)] += dynamic_table[(i, j, k)]
    

def count_lucky_numbers(limit):
    result = 0
    digits = map(int, str(limit))
    digits.reverse()
    sum_ = 0
    sqr_sum = 0
    for i in range(len(digits)-1, -1, -1):
        intermediate_result = 0
        for l in range(digits[i]):
            for j in range(9*i+1):
                if j+l+sum_ in primes:
                    for k in range(9*9*i+1):
                        if k+l*l+sqr_sum in primes:
                            intermediate_result += dynamic_table[(i, j, k)]
        result += intermediate_result
        
        sum_ += digits[i]
        sqr_sum += digits[i]**2
    
    if sum_ in primes and sqr_sum in primes:
        result += 1
    
    return result
    

def main():
    data = sys.stdin.read().splitlines()
    generate_dynamic_table()
    for x in data[1:]:
        A, B = map(int, x.split())
        print count_lucky_numbers(B) - count_lucky_numbers(A-1)
        
        
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()