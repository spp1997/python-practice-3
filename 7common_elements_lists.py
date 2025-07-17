def get_list_input(prompt):
    return list(map(int, input(prompt).split()))

# Input from user
list1 = get_list_input("Enter first list of numbers (space-separated): ")  # 1 2 3
list2 = get_list_input("Enter second list of numbers: ")    #2 3 4
list3 = get_list_input("Enter third list of numbers: ")    #3 2 5

# Convert to sets and find intersection
common_elements = list(set(list1) & set(list2) & set(list3))

print("Common elements:", common_elements)
