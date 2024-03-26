from tqdm import tqdm
import numpy as np

def triangle(n):
    """ returns the nth triangle number """
    return sum([i for i in range(1, n+1)])


def divisors(n):
    """ returns the divisors of n """
    factors = []
    for i in range(1, int(np.sqrt(n))+1):
        if (n % i == 0):
            factors.append(i)
            if (n // i != i):
                factors.append(n//i) 
            
            
    return sorted(factors)
    
def main():
    
    n  = 100000000
    
    for i in tqdm(range(n+1)):
        t = triangle(i)
        if len(divisors(t)) > 500:
            print(f"{i}: {t} - {len(divisors(t))}")  # 76576500
            break
    

if __name__ == "__main__":
    main()