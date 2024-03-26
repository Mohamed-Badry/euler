import math

def digit_sum(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    
    return sum

def main():
    
    print(digit_sum(math.factorial(100)))   # 648
    
    
if __name__ == "__main__":
    main()