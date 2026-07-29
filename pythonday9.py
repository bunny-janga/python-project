"""
=========================================================
PYTHON FUNCTIONS PRACTICE PROGRAMS
Topics Covered:
1. Default Arguments
2. Variable Length Positional Arguments (*args)
3. Variable Length Keyword Arguments (**kwargs)
4. *args and **kwargs Together
5. Local & Global Variables
6. Passing Arguments
7. Fibonacci Series


=========================================================
"""

# =========================================================
# Default Arguments
# =========================================================

# 1. Student Details

def StuDeta(name, age, course="MCA", city="Visakhapatnam"):
    print(f"Name   : {name}")
    print(f"Age    : {age}")
    print(f"Course : {course}")
    print(f"City   : {city}")

StuDeta(
    name=input("Name : "),
    age=int(input("Age : "))
)


# 2. Rectangle Area

def area(length, width=5):
    print("Area =", length * width)

area(int(input("Length : ")))


# =========================================================
# Variable Length Positional Arguments (*args)
# =========================================================

# 3. Sum of Numbers

def sum_numbers(*args):
    total = 0
    for num in args:
        total += int(num)
    print("Sum =", total)

numbers = input("Enter Numbers : ").split()
sum_numbers(*numbers)


# 4. Largest Number

def largest(*args):
    print("Largest =", max(args))

numbers = list(map(int, input("Enter Numbers : ").split()))
largest(*numbers)


# 5. Print Arguments

def print_values(*args):
    for value in args:
        print(value)

values = input("Enter Values : ").split()
print_values(*values)


# =========================================================
# Variable Length Keyword Arguments (**kwargs)
# =========================================================

# 6. Student Details

def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student_details(
    Name=input("Name : "),
    Age=int(input("Age : ")),
    Course=input("Course : ")
)


# 7. Employee Details

def employee_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

employee_details(
    Name="Rahul",
    Salary=35000,
    Department="Python"
)


# 8. Product Details

def product_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

product_details(
    Product="Laptop",
    Price=50000,
    Brand="HP"
)


# =========================================================
# *args and **kwargs Together
# =========================================================

# 9. Student Information

def student_info(*marks, **details):
    print("Marks :", marks)
    print(details)

student_info(
    85, 90, 88,
    Name="Bunny",
    Age=24
)


# 10. Mixed Arguments

def mixed_arguments(*args, **kwargs):
    print(args)
    print(kwargs)

mixed_arguments(
    10, 20, 30,
    name="Bunny",
    city="Vizag"
)


# =========================================================
# Local and Global Variables
# =========================================================

# 11. Local and Global Variable

num = 23

def local_global(value):
    local_num = 20
    print("Local Variable :", local_num)
    print("Global Variable :", value)

local_global(num)


# 12. Access Global Variable

number = 100

def display_global():
    print("Global Variable =", number)

display_global()


# =========================================================
# Passing Arguments
# =========================================================

# 13. Passing by Value

def values(a, b):
    print(a, b)

values(10, 20)


# 14. Passing User Input

def addition(a, b):
    print("Sum =", a + b)

addition(
    int(input("Enter First Number : ")),
    int(input("Enter Second Number : "))
)


# =========================================================
# Fibonacci Series
# =========================================================

first = 0
second = 1

limit = int(input("Enter Number of Terms : "))

def fibonacci(first, second, limit):
    print(first, second, end=" ")

    for i in range(limit - 2):
        total = first + second
        first = second
        second = total
        print(total, end=" ")

fibonacci(first, second, limit)