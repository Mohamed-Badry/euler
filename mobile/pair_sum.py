def pair_sum(a, sum):
    a.sort()
    i = 0
    j = -1
    for _ in enumerate(a):
        x = a[i]
        y = a[j]
        if x + y > sum:
            j -= 1
        elif x + y < sum:
            i += 1
        else:
            return f"The pair: {x}, {y}"
    no_pair_found = f"No pair in this list has a sum of {sum}"
    return no_pair_found

arr = [1,2,4,4,6,3,1,3,5,17,18,11,6,7,8]
sum = 6
        
print(pair_sum(arr, sum))