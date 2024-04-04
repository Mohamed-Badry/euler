def sum_of_nth_powers_digits(number:int, n:int) -> bool:
    """
    checks whether a number can be written as a the sum of nth powers of their digits 
    where n is given by user
    parameters:
        number: the number you want to check
        n: the power 
    """
    # edge cases as they fulfill the conditions but aren't a sum
    if number == 1 or number == 0:
        return False
    
    digit_list = [int(digit) for digit in str(number)]
    power_sum = 0
    for d in digit_list:
        power_sum += d**n
    
    if power_sum == number:
        return True
    return False
    
    
def main():
    
    # I didn't try to prove it but I assumed that numbers above a million would be
    # less likely to fulfill the conditions as 999999 would only result in a fifth power sum
    # of 354294 which is way below the actual number
    upper_bound = int(1e6)  
    power = 5
    result_list = []
    for i in range(upper_bound):
        if sum_of_nth_powers_digits(i, power):
            result_list.append(i)
            
    for res in result_list:
        print(res)
        
    print(sum(result_list)) # 443839
    

if __name__ == "__main__":
    main()