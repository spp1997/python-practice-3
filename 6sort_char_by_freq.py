from collections import Counter

def sort_by_frequency(s):
    freq = Counter(s)
    sorted_chars = sorted(freq.items(), key=lambda x: -x[1])
    result = ''.join(char * count for char, count in sorted_chars)
    return result

# Input from user
user_input = input("Enter a string: ")    #banana
output = sort_by_frequency(user_input)
print("Sorted by descending frequency:", output)
