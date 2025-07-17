def words_starting_with_vowel(sentence):
    vowels = 'aeiouAEIOU'
    words = sentence.split()
    result = [word for word in words if word[0] in vowels]
    return result

# Input from user
sentence = input("Enter a sentence: ")    #Apple is an orange fruit  

# Get and print result
vowel_words = words_starting_with_vowel(sentence)
print("Words starting with a vowel:", ', '.join(vowel_words))
