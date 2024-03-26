from math import sqrt

def is_prime(n):
    for i in range(2,int()):
        if n % i == 0:
            return False
    return True
                
      
def largest_prime_factor(n):
    for i in range(int(n/2),2,-1):
        if n % i == 0:
            if is_prime(i):
                return i
            

  
n = 600851
print(' ',largest_prime_factor(n))