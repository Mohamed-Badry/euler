def Fibo(a=[1,1], n=1):
    length = len(a)
    if n == 1:
        return a[0]
    for i in range(length-1, n):
        if len(a) == n:
            return a[n-1]
        a.append(a[-1] + a[-2])
        
def main():
    
    arr = [1, 1]
    for i in range(1, 10000):
        f = Fibo(arr, i)
        if len(str(f)) == 1000: 
            print(f'{i}: {f}')
            break
            
#4782 for 1000 digits 
#47847 for 10000 digits   
    
if __name__ == '__main__':
    main()