import numpy 
import math
from itertools import permutations

def prime(upto=2000000):
    primes=numpy.arange(3,upto+1,2)
    isprime=numpy.ones((upto-1)//2,dtype=bool)
    for factor in primes[:int(math.sqrt(upto))//2]:
        if isprime[(factor-2)//2]:
            isprime[(factor*3-2)//2::factor]=0
    return numpy.insert(primes[isprime],0,2)
    
def main():               
    primes = prime(17)
    nums = []
    perms = list(permutations("0123456789", 10))
    for perm in perms:
        divisible = True
        for i in range(1,8):
            d = int(f'{perm[i]}{perm[i+1]}{perm[i+2]}')
            # print(' ', d, '  ', primes[i-1])
            if d % primes[i-1] != 0:
                divisible = False
        if divisible:
            nums.append(int(''.join(perm)))
        
    print(sum(nums))
    #16695334890
    
if __name__ == '__main__':
    main()