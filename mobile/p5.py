def smallest_multiple(n):
    if (n<=2):
      return n
    i = n * 2
    factors = [number  for number in range(n, 1, -1) if number * 2 > n]
    print(factors)

    while True:
        for a in factors:
            if i % a != 0:
                i += n
                break
            if (a == factors[-1] and i % a == 0):
                return i

s = smallest_multiple(20)       
print(' ',s)
print("Done!")
#[20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
#232792560
                                                  