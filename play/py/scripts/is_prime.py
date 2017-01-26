# http://spyhce.com/blog/taming-regular-expressions

import re

def is_prime0(n):
    return re.match(r'^1?$|^(11+?)\1+$', "1" * n) == None;


def is_prime(n):
    if n < 2:
        return False
    if n >= 2:
        for x in range(2, n):
            if n % x == 0:
                return False
    return True

if __name__ == '__main__':
    for i in range(50):
        s = ''
        if is_prime(i):
            s = '*'
        print('{} - {}'.format(i, s))
