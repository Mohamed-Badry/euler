from itertools import combinations
from multiprocessing import Process
from tqdm import tqdm
from math import sqrt

def amicable(p, q):
    if d(p) == q and d(q) == p and p != q:
        return True

def d(n):
    sum = 1
    for i in range(2, int(sqrt(n))):
        div = n / i
        if div % 1 == 0:
            sum += int(n/div)
            sum += int(div)
    return sum

def amicable_nums_sum(combs):
    result = set()
    
    for i, j in tqdm(combs):
        if amicable(i, j):
            result.add(i)
            result.add(j)
            print(' ', i, ' ',  j)
    return result
                        
def test(combs):
    
    result = amicable_nums_sum(combs)
    print(result)
    
if __name__ == '__main__':
    process_list = []
    combs = list(combinations(range(1, 10000), 2))
    l = len(combs)
    step=l//10
    for i in range(0, l, step):
        process = Process(target=test(combs[i:i+step]))
        process_list.append(process)
        
    for process in process_list:
        process.start()
    
    for process in process_list:
        process.join()
        