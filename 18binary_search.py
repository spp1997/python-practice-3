def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Not found

# Input from user
arr = list(map(int, input("Enter a sorted list of numbers: ").split()))     #1 2 3 4 5
target = int(input("Enter the target number: "))       #4

# Perform binary search
index = binary_search(arr, target)

# Output the result
if index != -1:
    print(f"Index: {index}")
else:
    print("Element not found.")
