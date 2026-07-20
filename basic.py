
# 1. Python Overview
num = "yash"
print(type(num))
num = 9
print(type(num))
num = [5, 6]
print(type(num))

# 2. Comments
# Single-line comment
"""Multi-line comment"""

# 3. Variables
_num = 90
num = 9
Num = 99
num_2 = 7
print(_num, num, Num, num_2)

# 4. Boolean Type
num = 7
num_2 = 77
print(num == num_2)
print(num != num_2)

# 5. Multiple Variables - Same Value
num = num_2 = num_3 = 77
print(num, num_2, num_3)

# 6. Multiple Variables - Different Values
num, num_2 = 7, 77
print(num, num_2)

# 7. Swapping Variables
num = 7
num_2 = 77
num, num_2 = num_2, num
print(num, num_2)
