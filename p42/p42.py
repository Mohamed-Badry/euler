def word_value(word: str) -> int:
    """ returns value of word based on position of its letters in the alphabet """
    sum = 0
    for letter in word.upper():
        letter_value = ord(letter) - ord('A') + 1
        sum += letter_value
    
    return sum


def triangle_nums(upto: int=100) -> list[int]:
    triangle_list = []
    for i in range(upto):
        triangle_list.append((1/2) * i * (i + 1))
    
    return triangle_list


def main():
    upper_bound = 100
    triangle_list = triangle_nums(upper_bound)
    with open('words.txt', 'r') as f:
        words = f.read().split(',')
        words = [word.strip('\"') for word in words]
        
        count = 0   
        for word in words:
            if word_value(word) in triangle_list:
                count += 1
                
        print(f"Count of triangle words {count}")  # 162
        
        
if __name__ == "__main__":
    main()