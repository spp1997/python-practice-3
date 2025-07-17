def sum_of_digits_in_string(input_str):
    total = 0
    for ch in input_str:
        if ch.isdigit():
            total += int(ch)
    return total

# Input from user
user_input = input("Enter a string: ")
#a1b2c3

# Call the function and print result
print("Sum of digits:", sum_of_digits_in_string(user_input))
