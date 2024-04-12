import numpy as np
from tqdm import tqdm
from math import sqrt


def prime(upto=2000000):
    primes=np.arange(3,upto+1,2)
    isprime=np.ones((upto-1)//2,dtype=bool)
    for factor in primes[:int(sqrt(upto))//2]:
        if isprime[(factor-2)//2]:
            isprime[(factor*3-2)//2::factor]=0
    return np.insert(primes[isprime],0,2)


def is_pandigital(num:int) -> bool:
    """ 
    checks if number is pandigital from 1 to l where l
    is the length of the number 
    """
    num_list = [int(n) for n in str(num)]
    l = len(num_list)
    
    if 0 in num_list or l > 9 or l == 0:
        return False
    
    check_list = list(range(1, l+1))
    for n in num_list:
        if n in check_list:
            check_list.remove(n)
        else:
            return False
    if len(check_list) == 0:
        return True
    
    
def main():
    
    upper_bound = int(1e9)
    prime_list = prime(upper_bound)
    
    results = []
    for num in tqdm(prime_list):
        if is_pandigital(int(num)):
            results.append(num)
    
    print(results)
    print(max(results))     # 7652413
    

    
if __name__ == "__main__":
    main()