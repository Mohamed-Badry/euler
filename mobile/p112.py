def increasing(n):
    for i, num in enumerate(n):
        if i == 0:
            i = 1
        if int(num) < int(n[i-1]):
            return False
    return True

def decreasing(n):
    for i, num in enumerate(n):
        if i == 0:
            i = 1
        if int(num) > int(n[i-1]):
            return False
    return True

def bouncy(n):
    if decreasing(n) or increasing(n):
        return False
    return True

count = 0
p = 0.99

for num in range(10000000):
    if bouncy(str(num)):
        count += 1
        prop = (count/num)
        if prop == p:
            print(f'Least number for which proportion reaches {p} is {num}')
            print(f'Proportion = {prop}')
            print(f'Count = {count}')
            break
        

#Least number for which proportion reaches 0.99 is 1587000
#Proportion = 0.99
#Count = 1571130