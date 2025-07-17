def is_sorted_ascending(lst):
    return lst == sorted(lst)

# Input from user
lst = list(map(int, input("Enter a list of numbers (space-separated): ").split()))     # Example input: 1 2 3 4 5     1 2 3 5 4  

# Check and print result
print("Is the list sorted in ascending order?", is_sorted_ascending(lst))
