import re
from num2words import num2words

def num_word_length(n):
    """ returns the length of the word for number n """
    l = 0
    # print(n)
    for word in re.split("-|,| ", num2words(n)):
        # print(f"{word}")
        l += len(word)
        
    return l


def main():
    
    n = 1000
    sum = 0
    for i in range(1, n+1):
        sum += num_word_length(i)
    
    print(f"sum: {sum}") # 21124
        
if __name__ == "__main__":
    main()