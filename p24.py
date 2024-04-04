from itertools import permutations

def main():
    n = 9
    nums = list(range(n+1))
    
    perms = permutations(nums, n+1)
    sorted_concat_perms = [''.join([str(n) for n in perm]) for perm in perms]
    
    for i, perm in enumerate(sorted_concat_perms, start=1):
        if i == 1e6:
            print(perm)  # 2783915460
            break

if __name__ == "__main__":
    main()