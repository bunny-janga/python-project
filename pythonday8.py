
# =========================================================
# 1. Even or Odd Numbers in a Range
# =========================================================

def even_odd_range():
    limit = int(input("Enter the limit: "))

    for number in range(1, limit + 1):
        if number % 2 == 0:
            print(f"{number} is Even")
        else:
            print(f"{number} is Odd")


# =========================================================
# 2. Prime Number Check
# =========================================================

def prime_check():
    number = int(input("Enter a number: "))

    if number <= 1:
        print("Not a Prime Number")
        return

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print(f"{number} is Not a Prime Number")
            return

    print(f"{number} is a Prime Number")


# =========================================================
# 3. Generate Prime Numbers Till 100
# =========================================================

def prime_till_100():
    print("Prime Numbers from 1 to 100:\n")

    for number in range(2, 101):
        is_prime = True

        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                is_prime = False
                break

        if is_prime:
            print(number, end=" ")

    print()


# =========================================================
# 4. Reverse String & Palindrome
# =========================================================

def reverse_palindrome():
    text = input("Enter a word: ")

    reverse = text[::-1]

    print("Reverse :", reverse)

    if text == reverse:
        print("Palindrome")
    else:
        print("Not a Palindrome")


# =========================================================
# 5. Right Angle Triangle - Stars
# =========================================================

def right_triangle_star():
    rows = int(input("Enter number of rows: "))

    for i in range(1, rows + 1):
        print("*" * i)


# =========================================================
# 6. Right Angle Triangle - Stars (Nested Loop)
# =========================================================

def right_triangle_nested():
    rows = int(input("Enter number of rows: "))

    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end=" ")
        print()


# =========================================================
# 7. Right Angle Triangle - Numbers
# =========================================================

def right_triangle_numbers():
    rows = int(input("Enter number of rows: "))

    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


# =========================================================
# 8. Right Angle Triangle - Continuous Numbers
# =========================================================

def continuous_numbers():
    rows = int(input("Enter number of rows: "))

    count = 1

    for i in range(1, rows + 1):
        for j in range(i):
            print(count, end=" ")
            count += 1
        print()


# =========================================================
# 9. Inverted Right Triangle - Stars
# =========================================================

def inverted_star():
    rows = int(input("Enter number of rows: "))

    for i in range(rows, 0, -1):
        print("* " * i)


# =========================================================
# 10. Inverted Right Triangle - Numbers
# =========================================================

def inverted_numbers():
    rows = int(input("Enter number of rows: "))

    for i in range(rows, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


# =========================================================
# 11. Inverted Continuous Numbers
# =========================================================

def inverted_continuous():
    rows = int(input("Enter number of rows: "))

    count = 1

    for i in range(rows, 0, -1):
        for j in range(i):
            print(count, end=" ")
            count += 1
        print()


# =========================================================
# 12. Pyramid Pattern
# =========================================================

def pyramid():
    rows = int(input("Enter number of rows: "))

    for i in range(rows):
        print(" " * (rows - i - 1), end="")
        print("* " * (i + 1))

    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i), end="")
        print("* " * i)


# =========================================================
# 13. Remove Duplicates from List
# =========================================================

def remove_duplicates():
    numbers = [1, 2, 3, 3, 4, 4]

    unique = []

    for item in numbers:
        if item not in unique:
            unique.append(item)

    print("Original List :", numbers)
    print("Unique List   :", unique)


# =========================================================
# 14. Perfect Number
# =========================================================

def perfect_number():
    number = int(input("Enter a number: "))

    total = 0

    for i in range(1, number):
        if number % i == 0:
            total += i

    if total == number:
        print(f"{number} is a Perfect Number")
    else:
        print(f"{number} is Not a Perfect Number")


# =========================================================
# Main Menu
# =========================================================

def main():
    while True:
        print("\n========== Python Programs ==========")
        print("1. Even or Odd")
        print("2. Prime Check")
        print("3. Prime Numbers Till 100")
        print("4. Reverse & Palindrome")
        print("5. Right Triangle Stars")
        print("6. Right Triangle Stars (Nested)")
        print("7. Right Triangle Numbers")
        print("8. Continuous Numbers")
        print("9. Inverted Triangle Stars")
        print("10. Inverted Triangle Numbers")
        print("11. Inverted Continuous Numbers")
        print("12. Pyramid Pattern")
        print("13. Remove Duplicates")
        print("14. Perfect Number")
        print("0. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            even_odd_range()
        elif choice == "2":
            prime_check()
        elif choice == "3":
            prime_till_100()
        elif choice == "4":
            reverse_palindrome()
        elif choice == "5":
            right_triangle_star()
        elif choice == "6":
            right_triangle_nested()
        elif choice == "7":
            right_triangle_numbers()
        elif choice == "8":
            continuous_numbers()
        elif choice == "9":
            inverted_star()
        elif choice == "10":
            inverted_numbers()
        elif choice == "11":
            inverted_continuous()
        elif choice == "12":
            pyramid()
        elif choice == "13":
            remove_duplicates()
        elif choice == "14":
            perfect_number()
        elif choice == "0":
            print("Thank you!")
            break
        else:
            print("Invalid Choice. Try Again.")


if __name__ == "__main__":
    main()