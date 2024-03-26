from itertools import combinations
import time

def largest_palindrome(k):
    '''
    input: k (int) number of digits
    
    output: returns the largest palindrome number made from the product of k digit numbers (int)
    '''    
    
    x_arr = [x for x in range(int((10**(k)-(10**(k-1)))),10**k)]
    comb = combinations(x_arr, 2)
    arr = []
    
    #iterates over the combinations and unpacks them into x and y
    for i in comb:
        x = i[0]
        y = i[1]
        z = str(x*y)
        n = len(z)
        
        #checks if the digits of the input are even or odd and slices it accordingly
        if n % 2 == 0:
            condition = (z[:int(n/2)] == z[int(n/2):][::-1])
        else:
            condition = (z[:int(n/2)] == z[int(n/2)+1:][::-1])
            
        if condition:
             #print(' ',i,z)
             arr.append(int(z))
             
    return max(arr)

num = int(input("Number of digits: "))

start = time.time()
print(f"\nThe largest palindrome of products of {num} digit numbers is: {largest_palindrome(num)}")    
end = time.time()

print(f"\nThis operation took: {end - start:.5f} seconds")