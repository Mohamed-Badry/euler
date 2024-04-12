from functools import cache
from tqdm import tqdm 

@cache
def factorial(n: int) -> int:
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n - 1)
    
def equal_to_fac_sum_of_digits(n: int) -> bool:
    """ checks if sum of factorials of the digits of n is equal to n """
    if n == 1 or n == 2:
        return False
    digits = [int(num) for num in str(n)]
    fac_digits = [factorial(num) for num in digits]
    if n == sum(fac_digits):
        return True
    return False
    

def main():
    
    upper_bound = 1_000_000
    results = []
    for i in tqdm(range(upper_bound)):
        if equal_to_fac_sum_of_digits(i):
            results.append(i)
    
    print(results)          # [145, 40585]
    print(sum(results))     # 40730

if __name__ == "__main__":
    main()