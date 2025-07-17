# Input from user
keys = input("Enter list of keys (space-separated): ").split()      # a b
values = input("Enter list of values (space-separated): ").split()   # 1 2

# Convert values to integers (optional, if they are numbers)
values = [int(v) for v in values]

# Combine using zip
result = dict(zip(keys, values))

print("Combined dictionary:", result)
