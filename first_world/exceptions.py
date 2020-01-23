# try:
#     # file = open("app.py")
#     with open("app.py") as file:  # closes resources auto
#         print("File opened.")
#         file.__enter__
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age.")
# except ZeroDivisionError:
#     print("Age cannot be zero.")
# else:
#     print("No exceptions were thrown.")
# finally:
#     file.close()  # release external resourses
# print("Execution continues.")

# Raising exceptions
from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10/ age

try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""

print("first code=", timeit(code1, number=10000))
