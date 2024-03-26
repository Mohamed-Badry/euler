def self_powers(n=10):
    sum = 0
    for i in range(1,n+1):
        sum+= i**i
    return sum
    
print(str(self_powers(1000))[-10:])

#9110846700
 