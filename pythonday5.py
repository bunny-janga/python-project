# Integer Input

n = int(input("Enter an integer: "))
print(n + 9)
print(type(n))


# String Input

m = input("Enter anything: ")
print(m)
print(type(m))


# List of Integers

n = list(map(int, input("Enter integers: ").split()))
print(n)


# List of Strings

n = input("Enter words: ").split()
print(n)


# Tuple of Integers

n = tuple(map(int, input("Enter integers: ").split()))
print(n)


# Eval Input

num = eval(input("Enter: "))
print(type(num))


# String Reverse

n = "python"
m = n[::-1]
print(m)


# 24-Hour Clock to Normal Time

m = input("Enter 24-hour clock (HH:MM): ")
hour, minute = map(int, m.split(":"))

if hour == 0:
    hour = 12
    period = "AM"
elif hour < 12:
    period = "AM"
elif hour == 12:
    period = "PM"
else:
    hour = hour - 12
    period = "PM"

print(f"{hour}:{minute:02d} {period}")


# Character Frequency

s = input("Enter a string: ")
freq = {}

for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print(freq)

max_freq = max(freq.values())
print(max_freq)

for char in s:
    if freq[char] == max_freq:
        print(char)
        break