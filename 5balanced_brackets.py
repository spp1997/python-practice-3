def is_balanced(expression):
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != bracket_map[char]:
                return "Not Balanced"
            stack.pop()

    return "Balanced" if not stack else "Not Balanced"

# Input from user
user_input = input("Enter a string with brackets: ")
#[()]{}{[()()]()}
#[(])

# Check and print result
print(is_balanced(user_input))
