# ELIF STATEMENT

marks = int(input("Enter marks: "))

if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B+")
elif marks >= 60:
    print("B")
elif marks >= 50:
    print("C+")
elif marks >= 40:
    print("C")
elif marks >= 35:
    print("D")
else:
    print("Fail")


# GREATER VALUE OF THREE

A = int(input("Enter 1st NO: "))
B = int(input("Enter 2nd NO: "))
C = int(input("Enter 3rd NO: "))

if A > B and A > C:
    print(A, "is greater value")
elif B > A and B > C:
    print(B, "is greater value")
else:
    print(C, "is greater value")


# NESTED IF - ATM

detail_ = {"atmpin": "8520"}

atm_ = input("Enter 4 digit ATM pin: ")

if len(atm_) == 4:
    if atm_ == detail_["atmpin"]:
        op_ = int(input("Enter\n1. Withdraw\n2. Deposit\n3. Exit\n"))

        if op_ == 1:
            amount_w = int(input("Enter amount for withdrawal: "))
            print("Withdrawal amount:", amount_w)
        elif op_ == 2:
            amount_d = int(input("Enter amount for deposit: "))
            print("Deposit amount:", amount_d)
        elif op_ == 3:
            print("Thank you")
        else:
            print("Invalid option")
    else:
        print("Incorrect ATM pin entered")
else:
    print("Please enter 4 digit ATM pin")


# CONTINUE STATEMENT

num = [10, 20, 30, 40, 50]

for i in num:
    if i == 40:
        continue
    print(i)
else:
    print("End")


# PASS STATEMENT

num = [10, 20, 30, 40, 50]

for i in num:
    pass
else:
    print("End")


# FOR LOOP

num = "python"

for i in num:
    print(i)
else:
    print("End")


# RANGE FUNCTION

for i in range(2, 11, 2):
    print(i)


# FOR LOOP WITH BREAK

num = [10, 20, 30, 40, 50]

for i in num:
    print(i)
    if i == 40:
        break
else:
    print("End")


# WHILE LOOP

n = 1

while n < 10:
    n += 1
    print(n)


# ASSERT KEYWORD

age = 22

assert age >= 18, "Not eligible"

print("Eligible")


# 24-HOUR TIME TO 12-HOUR TIME

n = tuple(map(int, input("Enter 24h time: ").split(":")))

if n[0] >= 12 and n[0] <= 24:
    if n[0] == 12:
        print(f"{n[0]}:{n[1]} PM")
    else:
        print(f"{n[0] - 12}:{n[1]} PM")
else:
    print(f"{n[0]}:{n[1]} AM")