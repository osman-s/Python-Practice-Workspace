# Data Structures
# 1 - Lists
letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
zeros = [0] * 5
combined = zeros + letters
numbers = list(range(20))
chars = list("Hello World")
print(len(chars))

# 2 - Accessing Items
print(letters[0])
print(letters[-1])

letters[0] = "A"
print(letters[0:3])
print(letters[0:3])
print(numbers[::2])  # Steps through list
print(numbers[::-1])  # Reverses lists

# 3 - List Unpacking
numbers = [1, 2, 3, 4, 4, 4, 9]
first, second, *other, last = numbers
print(first, last)
print(other)

# 4 - Looping over Lists
# items = (0, "a")
# index, letter = items
for index, letter in enumerate(letters):
    print(index, letter)

# 5 - Adding or Removing Items
letters = ["a", "b", "c"]

# Add
letters.append("d")
letters.insert(0, "-")


# Remove
letters.pop(0)
letters.remove("b")
del letters[0:3]
letters.clear()  # deletes all objects in a list
print(letters)

# 6 - Finding Items
letters = ["a", "b", "c"]
print(letters.count("d"))
if "d" in letters:
    print(letters.index("d"))

# 7 - Sorting Lists
numbers = [3, 51, 2, 8, 6]
# numbers.sort(reverse=True)
print(sorted(numbers, reverse=True))  # Doesn't modify the original list
print(numbers)

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)

# 8 - Lambda Functions
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]
# shorter and easier way to describe a function that is only used once
items.sort(key=lambda item: item[1])
print(items)
