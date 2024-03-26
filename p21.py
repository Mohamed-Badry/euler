from itertools import combinations
from rich.progress import Progress

def amicable(p, q):
    if d(p) == q and d(q) == p and p != q:
        return True

def d(n):
    sum = 1
    for i in range(2, n):
        div = n / i
        if div % 1 == 0:
            sum += int(div)
    return sum
                
def main():
    result = set()
    combs = combinations(range(1, 10000), 2)
    
    with Progress() as progress:
        
        task = progress.add_task("[red]Computing...", total=10000)
        
        for i, j in combs:
            if amicable(i, j):
                result.add(i)
                result.add(j)
                print(' ', i, ' ',  j)
            progress.update(task, advance=0.0001)
        print(' ', sum(result))            
    
if __name__ == '__main__':
    main()
