# Prompt the user for a sentence
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Initialize a list to store palindromic words
palindromes = []

# Check each word for palindrome property
for word in words:
    if word.lower() == word[::-1].lower():  # Case-insensitive check
        palindromes.append(word)

# Print the result
if palindromes:
    print("Palindromic words:", ", ".join(palindromes))
else:
    print("No palindromic words found.")
