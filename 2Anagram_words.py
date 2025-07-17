def are_anagrams_by_dict(str1, str2):
    if len(str1) != len(str2):
        return False
    
    count1 = {}
    count2 = {}
    
    for ch in str1:
        count1[ch] = count1.get(ch, 0) + 1
    
    for ch in str2:
        count2[ch] = count2.get(ch, 0) + 1
    
    return count1 == count2

# Input from user
str1 = input("Enter the first string: ").replace(" ", "").lower()
str2 = input("Enter the second string: ").replace(" ", "").lower()

print("Are the strings anagrams (using dictionary)?", are_anagrams_by_dict(str1, str2))
