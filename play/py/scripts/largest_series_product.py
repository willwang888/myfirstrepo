"""
http://exercism.io/exercises/python/largest-series-product/readme
"""
import sys
import operator
import functools

a = '1027839564'
n = 5

#a = sys.argv[1]
#n = sys.argv[2]
#n = int(n)

def get_all_substrings(s, n=1):
    l = len(s)
    return [ s[i:j+1] for i in range(l) for j in range(i, l)
            if n == len(s[i:j+1]) ]

def get_product(a):
    return functools.reduce(operator.mul,
        [ int(i) for i in list(a) ]   )

def get_res(a, n):
 #   return max( get_product(i) for i in get_all_substrings(a, n)  )
    res = 1
    ind = []
    for i in get_all_substrings(a, n):
        p = get_product(i)
        if p  > res:
            res = p
            ind = i
    return (res, ind)

def largest_product(a, n):
    if n == 0 or len(a) == 0:
        return 1
    if a == "":
        raise ValueError('given string empty!')

    return max( get_product(i) for i in get_all_substrings(a, n) )

if __name__ == '__main__':
    print(a)
    print( get_all_substrings(a, n) )
    print( get_res(a, n) )

