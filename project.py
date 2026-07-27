sbi_bunny = {
    'Name': 'bunny',
    'atm_pin': '8520',
    'Balance': 78500
}

transactions = []
rem = 3

while rem > 0:
    pin = input("Enter 4 digit pin: ")

    if len(pin) == 4:

        if pin == sbi_bunny['atm_pin']:

            print("---------------------------------")
            print("_______ ATM Simulation _______")
            print("---------------------------------")

            op = int(input(
                "\n1.Check Balance\n2.WithDraw\n3.Deposit\n4.Transaction History\n5.Pin Change\nEnter Your Choice: "
            ))

            if op == 1:

                print("Your Current Balance = $", sbi_bunny['Balance'])

            elif op == 2:

                amount = int(input("Enter amount to withdraw: $"))

                if amount <= sbi_bunny['Balance'] and amount % 100 == 0:

                    sbi_bunny['Balance'] -= amount
                    transactions.append(f"Withdraw : ${amount}")

                    print("Collect your cash")
                    print("Remaining Balance = $", sbi_bunny['Balance'])

                else:

                    if amount <= 0:
                        print("Invalid Amount")

                    elif amount > sbi_bunny['Balance']:
                        print("Insufficient Funds")

                    else:
                        print("Enter amount in multiples of 100")

            elif op == 3:

                amount = int(input("Enter amount to deposit: $"))

                if amount > 0 and amount % 100 == 0:

                    sbi_bunny['Balance'] += amount
                    transactions.append(f"Deposit : ${amount}")

                    print("Amount Deposited Successfully")
                    print("Updated Balance = $", sbi_bunny['Balance'])

                else:

                    print("Invalid Amount")

            elif op == 4:

                if not transactions:

                    print("No Transactions Found")

                else:

                    print("Transaction History")

                    for i in transactions:
                        print(i)

            elif op == 5:

                old_pin = input("Enter Old Pin: ")

                if old_pin == sbi_bunny['atm_pin']:

                    new_pin = input("Enter New Pin: ")
                    confirm_pin = input("Confirm New Pin: ")

                    if len(new_pin) == 4 and new_pin.isdigit():

                        if new_pin == confirm_pin:

                            sbi_bunny['atm_pin'] = new_pin

                            print("PIN Changed Successfully")

                        else:

                            print("PIN Did Not Match")

                    else:

                        print("PIN Should Be 4 Digits")

                else:

                    print("Incorrect Current PIN")

            else:

                print("Invalid Choice")

            op1 = int(input(
                "\n_____ ATM Page _____\n1.Home\n2.Exit\nEnter Choice: "
            ))

            if op1 == 1:
                continue

            elif op1 == 2:
                print("Thank You For Using SBI ATM")
                break

            else:
                print("Invalid Choice")

        else:

            rem -= 1

            if rem > 0:
                print(f"Incorrect PIN. {rem} Attempts Left")

            else:
                print("Card Blocked")

    else:

        print("Please Enter Only 4 Digit PIN")