import math

print("Hello World")
x = 1
y = 2
uni_price = 3
course_name = """
Multiple
Lines
"""

x, y = 1, 2

z = w = 3
print(type(z))
print(len(course_name))

first = "Osman"
last = "Hasan"
full = f"{first} {last}"
# formatted Strings
print(full)

course = " Python"
print(course.upper())
print(course.strip())
print("Python" in course)
print("Python" not in course)
# Can represent numbers in binary or hex or even complect numbers
x = 1 + 2j
print(x)
x = x + 1
x += 1
# Upper case letter for variables that stay constant
PI = 3.14
print(PI)
print(math.floor(PI))

# x = input("x: ")
# y = x + 1

age = 22
if age == 19:
    print("no")
elif age >= 12:
    print("yes")

if z > 1:
    pass
else:
    pass

#  Logical operators
if 18 < age <= 65:
    print("Eligible")

# message = age >= 18 ? "Eligible": "Not Eligible"
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)
