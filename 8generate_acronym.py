def generate_acronym(phrase):
    words = phrase.split()
    acronym = ''.join(word[0].upper() for word in words if word)
    return acronym

# Input from user
user_input = input("Enter a phrase: ")
#Hyper Text Markup Language
print("Acronym:", generate_acronym(user_input))
