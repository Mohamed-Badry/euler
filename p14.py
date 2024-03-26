import operator as op
from tqdm import tqdm

def collatz(n, seq=None):
    if seq is None:
        seq = []
    seq.append(n)
    
    if n == 1:
        return seq
    
    if n % 2 == 0:
        return collatz(n//2, seq)
    else:
        return collatz(3*n+1, seq)
    
    
def main():
    
    s = 1
    n = int(1e6)
    chains = {}
    for i in tqdm(range(s, n)):
        chains[i] = len(collatz(i))
    
    sorted_chains = list(sorted(chains.items(), key=op.itemgetter(1), reverse=True))
    print(sorted_chains[0])     # (837799, 525)
        
if __name__ == "__main__":
    main()
