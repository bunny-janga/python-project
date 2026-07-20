# ==========================
# Sets
# ==========================

# 1. Create a set with duplicate values
so = {1, 2, 2, 3, 3, 4, 4, 5, 5}
print(so)

# 2. Create an empty set and print its data type
so = set()
print(so)
print(type(so))

# 3. Add a single element using add()
so = {1, 2, 3, 4}
so.add(5)
print(so)

# 4. Add multiple elements using update()
so = {1, 2, 3, 4}
so.update([5, 6])
print(so)

# 5. Remove an element using remove()
so = {1, 2, 3, 4, 5}
so.remove(2)
print(so)

# 6. Remove an element using discard()
so = {1, 2, 3, 4}
so.discard(2)
print(so)

# 7. Remove a random element using pop()
so = {1, 2, 3, 4, 5}
so.pop()
print(so)

# ==========================
# Set Operations
# ==========================

# 8. Union of two sets
a = {1, 2, 3, 4}
b = {2, 3, 5, 6, 7}
print(a | b)

# 9. Intersection of two sets
a = {1, 2, 3, 4}
b = {2, 3, 5, 6, 7}
print(a & b)

# 10. Difference between two sets
a = {1, 2, 3, 4}
b = {2, 3, 5, 6, 7}
print(a - b)
print(b - a)

# ==========================
# Type Conversion
# ==========================

# 11. Integer to string and float
a = 1
print(type(a))
b = str(a)
print(type(b))
c = float(a)
print(c)

# 12. Float to integer and string
a = 9.4
b = int(a)
c = str(a)
print(a, b, c)
print(type(a), type(b), type(c))

# 13. Numeric string to integer and float
a = "67"
b = int(a)
c = float(a)
print(a, b, c)
print(type(a), type(b), type(c))

# 14. String to list and tuple
a = "1234"
b = list(a)
c = tuple(a)
print(a, b, c)
print(type(a), type(b), type(c))

# 15. List to string and tuple
a = [1, 2, 3, 4]
b = str(a)
c = tuple(a)
print(a, b, c)
print(type(a), type(b), type(c))

# 16. Tuple to list and string
a = (1, 2, 3, 4, 5)
b = list(a)
c = str(a)
print(a, b, c)
print(type(a), type(b), type(c))

# ==========================
# Concatenation
# ==========================

# 17. Concatenate two strings
a = "python "
b = "is a high language"
print(a + b)

# 18. Concatenate two lists
a = [1, 2, 3, 4]
b = [4, 5, 6, 7]
print(a + b)

# 19. Concatenate two tuples
a = (1, 2, 3, 4, 5)
b = (9, 8, 7, 6)
print(a + b)

# 20. Integer addition vs string concatenation
a = 9
b = 8
c = "9"
d = "8"
print(a + b)
print(c + d)