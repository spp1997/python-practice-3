def rotate_right(lst, k):
    k = k % len(lst)  # Handle k > len(lst)
    return lst[-k:] + lst[:-k]

# Input from user
lst = list(map(int, input("Enter list elements (space-separated): ").split()))      #1 2 3 4 5
k = int(input("Enter number of steps to rotate: "))    #2

# Output the rotated list
rotated = rotate_right(lst, k)
print("Rotated list:", rotated)
