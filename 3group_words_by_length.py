def group_words_by_length(words):
    result = {}
    for word in words:
        length = len(word)
        if length not in result:
            result[length] = []
        result[length].append(word)
    return result

# Input from user
user_input = input("Enter words separated by space: ")
word_list = user_input.split()

# Call the function and print result
grouped = group_words_by_length(word_list)
print(grouped)
