# Data Structures
from pprint import pprint
from sys import getsizeof
from array import array
from collections import deque

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

# 9 - Map Function
prices = list(map(lambda item: item[1], items))
print(prices)

# 10 - Filter Function
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)

# 11 - List Comprehensions
prices = [item[1] for item in items]
print(prices)

filtered = [item for item in items if item[1] >= 10]
print(filtered)

# 12 - Zip Function
list1 = [1, 2, 3]
list2 = [10, 20, 30]

print(list(zip("abc", list1, list2)))

# 13 - Stacks 0 have LIFO behavior (Last in Last Out)
[1, 2, 3]
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop()
print(last)
print(browsing_session)
print("redirect", browsing_session[-1])
if not browsing_session:
    print("disabled")

# 14 Queues FIFO (First In First Out)
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)

if not queue:
    print("empty")

# 15 - Tuples: a read only list
point = (1, 2) + (3, 4)
print(type(point))
print(point)

# 16 - Swapping Variables
x = 10
y = 11

z = x
x = y
y = z
print("x", x)
print("y", y)

x, y = y, x  # Cool way to create tuple, then unpack variables to perform swap

# 17 - Arrays: only for a large sequence of numbers and performance issues
numbers = array("i", [1, 2, 3])
numbers.append(4)
print(numbers)

# 18 - Sets: unordered collections of unique items
numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 5}
print(first | second)  # union of two sets
print(first & second)  # in both
print(first - second)  # difference
print(first ^ second)  # in one or the other
# can't access using index

# 19 - Dictionaries: collection of key value pairs
point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
point["x"] = 10
point["z"] = 20
print(point)

print(point.get("a", 0))
del point["x"]
print(point)
for key in point:
    print(key, point[key])

for key, value in point.items():
    print(key, value)

# 20 - Dictionary Comprehensions
# values = []
# for x in range(5):
#     values.append(x*2)

# values = {}
# for x in range():
#     values[x] = x * 2

values = {x: x*2 for x in range(5)}  # Way simpler to write
print(values)

# 21 - Generator Expressions - can access when iterate ( won't know length)
values = (x * 2 for x in range(100000))
print("gen:", getsizeof(values))

values = [x * 2 for x in range(100000)]
print("list:", getsizeof(values))
# for x in values:
#     print(x)

# 22 Unpacking Operator
numbers = [1, 2, 3]
print(*numbers)
print(1, 2, 3)

values = list(range(5))
values = [*range(5), *"Hello"]

first = [1, 2]
second = [3]
values = [*first, "a", *second, *"Hello"]
print(values)

first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}
print(combined)

# 23 Exercise: Most repeated character in sentence
sentence = "This is a common interview question"
char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
char_frequency_sorted = sorted(
    char_frequency.items(),
    key=lambda kv: kv[1],
    reverse=True)
# pprint(char_frequency, width=1)
print(char_frequency_sorted[0])
