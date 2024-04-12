from tqdm import tqdm

def is_pandigital(nums:list) -> bool:
    """ checks if list of numbers is pandigital from 1 to 9 """
    l = len(nums)
    
    if 0 in nums or l != 9:
        return False
    
    check_list = list(range(1, 9+1))
    # print(check_list)
    for n in nums:
        if n in check_list:
            check_list.remove(n)
            # print(f"{n=}")
        else:
            return False
    # print(f"{len(check_list)=}")
    if len(check_list) == 0:
        return True
    
    
def main():
    
    # I assumed this upper bound based on the fact that the sum of the number of
    # digits can't exceed 9 though it's just a rough estimate and can be optimised further
    upper_bound = 10000    
    results = []
    for i in tqdm(range(1, upper_bound+1)):
        for j in range(1, upper_bound+1):
            prod = i * j
            num_str = str(i) + str(j) + str(prod)
            # print(num_str)
            num_list = [int(n) for n in num_str]
            if is_pandigital(num_list):
                results.append(prod)
                
    # eleminate duplicates
    results = list(set(results))
    print(results)          # [5346, 5796, 6952, 7852, 4396, 7632, 7254]
    print(sum(results))     # 45228
                
    
if __name__ == "__main__":
    main()