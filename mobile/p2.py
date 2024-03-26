def fibo(a=[1,1], n=1):
    length = len(a)
    if n == 1:
        return a[0]
    for i in range(length-1, n):
        if len(a) == n:
            return a[n-1]
        a.append(a[-1] + a[-2])

def main():
    arr = [1, 1]   
    x = []  
    for i in range(1, 34):
        f = fibo(arr, i)
        if f <= 4e6 and f%2 == 0:
             x.append(f)
    
    x.pop(0)
    
    print(sum(x))
    # 4613730
    
if __name__ == '__main__':
    main()