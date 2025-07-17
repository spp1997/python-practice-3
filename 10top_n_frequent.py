from collections import Counter

def top_n_frequent_elements(lst, n):
    freq = Counter(lst)
    most_common = freq.most_common(n)
    return [item for item, count in most_common]

# Input from user
lst = list(map(int, input("Enter a list of numbers (space-separated): ").split()))           #1 1 2 2 2 3
n = int(input("Enter value of N: "))      #2

# Output the result
result = top_n_frequent_elements(lst, n)
print("Top", n, "frequent elements:", result)
