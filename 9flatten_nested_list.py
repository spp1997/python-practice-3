def flatten_list(nested):
    flat = []
    for item in nested:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat

# Input from user
user_input = input("Enter a nested list (e.g., [1, [2, [3, 4]], 5]): ")    #[1, [2, [3, 4]], 5]
nested_list = eval(user_input)  # Note: Only use eval in trusted environments!

# Flatten and display
flattened = flatten_list(nested_list)
print("Flattened list:", flattened)
