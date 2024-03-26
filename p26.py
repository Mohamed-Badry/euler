import re
import numpy as np

from decimal import *
from tqdm import tqdm


def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n//3 + (n%6==2), dtype=bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]


def recurring(n):
    """ 
    finds (a permutation of) longest repeating substring in decimal number 
    
    the reason that this finds a permutation and not the first pattern you'd see is that it reverses the 
    number and works its way backwards to avoid missing numbers which don't start with the repeating pattern.
    Since the numbers would be infinitly repeating using a high enough precision and the decimal module should
    suffice to avoid weird cutoff errors.
    """
    # split the number on the decimal take the part after the decimal and reverse it
    num = str(n).split('.')[1][::-1]
    
    # match repeating patterns 
    pattern = r'(\d+?)\1+?(?=\d*?$)'
    match = re.search(pattern, num)
    
    if match:
        return match.group(1)[::-1]
    else:
        return '0'
    


def main():
    getcontext().prec = 10000000
    
    n = 1000
    d = {}
    
    # fix to work for numbers above 100
    for i in tqdm(primesfrom2to(n)):
        # print(100*'-')
        repeating = recurring(Decimal(1)/Decimal(int(i)))
        if repeating == '0':
            continue
        d[i] = repeating
    
    # print(d)
    sorted_dict = dict(sorted(d.items(), key=lambda item: len(item[1])))
    print(sorted_dict)
    print()
    m = max(sorted_dict.items(), key=lambda x: len(x[1]))
    print(m) # 983
    # 9967 for (d < 10000)
    

if __name__ == "__main__":
    main()