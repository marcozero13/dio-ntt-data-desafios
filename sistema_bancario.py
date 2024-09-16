menu = """

[d] Deposit
[w] Withdraw
[e] Statement
[q] Quit

=> """

balance = 0
limit = 500
statement = ""
num_withdrawals = 0
MAX_WITHDRAWALS = 3

while True:

    option = input(menu)

    if option == "d":
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            statement += f"Deposit: R$ {amount:.2f}\n"

        else:
            print("Operation failed! The amount provided is invalid.")

    elif option == "w":
        amount = float(input("Enter withdrawal amount: "))

        exceeded_balance = amount > balance

        exceeded_limit = amount > limit

        exceeded_withdrawals = num_withdrawals >= MAX_WITHDRAWALS

        if exceeded_balance:
            print("Operation failed! You do not have enough balance.")

        elif exceeded_limit:
            print("Operation failed! The withdrawal amount exceeds the limit.")

        elif exceeded_withdrawals:
            print("Operation failed! Maximum number of withdrawals exceeded.")

        elif amount > 0:
            balance -= amount
            statement += f"Withdrawal: R$ {amount:.2f}\n"
            num_withdrawals += 1

        else:
            print("Operation failed! The amount provided is invalid.")

    elif option == "e":
        print("\n================ STATEMENT ================")
        print("No transactions made." if not statement else statement)
        print(f"\nBalance: R$ {balance:.2f}")
        print("==========================================")

    elif option == "q":
        break

    else:
        print("Invalid operation, please select the desired operation again.")
