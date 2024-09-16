import textwrap


def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDeposit
    [w]\tWithdraw
    [s]\tStatement
    [nc]\tNew account
    [lc]\tList accounts
    [nu]\tNew user
    [q]\tExit
    => """
    return input(textwrap.dedent(menu))


def deposit(balance, amount, statement, /):
    if amount > 0:
        balance += amount
        statement += f"Deposit:\tR$ {amount:.2f}\n"
        print("\n=== Deposit completed successfully! ===")
    else:
        print("\n@@@ Operation failed! The amount entered is invalid. @@@")

    return balance, statement


def withdraw(*, balance, amount, statement, limit, number_of_withdrawals, withdrawal_limit):
    exceeded_balance = amount > balance
    exceeded_limit = amount > limit
    exceeded_withdrawals = number_of_withdrawals >= withdrawal_limit

    if exceeded_balance:
        print("\n@@@ Operation failed! Insufficient balance. @@@")

    elif exceeded_limit:
        print("\n@@@ Operation failed! The withdrawal amount exceeds the limit. @@@")

    elif exceeded_withdrawals:
        print("\n@@@ Operation failed! Maximum number of withdrawals exceeded. @@@")

    elif amount > 0:
        balance -= amount
        statement += f"Withdrawal:\tR$ {amount:.2f}\n"
        number_of_withdrawals += 1
        print("\n=== Withdrawal completed successfully! ===")

    else:
        print("\n@@@ Operation failed! The amount entered is invalid. @@@")

    return balance, statement


def display_statement(balance, /, *, statement):
    print("\n================ STATEMENT ================")
    print("No transactions were made." if not statement else statement)
    print(f"\nBalance:\tR$ {balance:.2f}")
    print("===========================================")


def create_user(users):
    cpf = input("Enter CPF (numbers only): ")
    user = filter_user(cpf, users)

    if user:
        print("\n@@@ A user with this CPF already exists! @@@")
        return

    name = input("Enter full name: ")
    birth_date = input("Enter date of birth (dd-mm-yyyy): ")
    address = input("Enter address (street, number - neighborhood - city/state abbreviation): ")

    users.append({"name": name, "birth_date": birth_date, "cpf": cpf, "address": address})

    print("=== User created successfully! ===")


def filter_user(cpf, users):
    filtered_users = [user for user in users if user["cpf"] == cpf]
    return filtered_users[0] if filtered_users else None


def create_account(branch, account_number, users):
    cpf = input("Enter user CPF: ")
    user = filter_user(cpf, users)

    if user:
        print("\n=== Account created successfully! ===")
        return {"branch": branch, "account_number": account_number, "user": user}

    print("\n@@@ User not found, account creation process terminated! @@@")


def list_accounts(accounts):
    for account in accounts:
        line = f"""\
            Branch:\t\t{account['branch']}
            Account:\t{account['account_number']}
            Holder:\t\t{account['user']['name']}
        """
        print("=" * 100)
        print(textwrap.dedent(line))


def main():
    WITHDRAWAL_LIMIT = 3
    BRANCH = "0001"

    balance = 0
    limit = 500
    statement = ""
    number_of_withdrawals = 0
    users = []
    accounts = []

    while True:
        option = menu()

        if option == "d":
            amount = float(input("Enter deposit amount: "))

            balance, statement = deposit(balance, amount, statement)

        elif option == "w":
            amount = float(input("Enter withdrawal amount: "))

            balance, statement = withdraw(
                balance=balance,
                amount=amount,
                statement=statement,
                limit=limit,
                number_of_withdrawals=number_of_withdrawals,
                withdrawal_limit=WITHDRAWAL_LIMIT,
            )

        elif option == "s":
            display_statement(balance, statement=statement)

        elif option == "nu":
            create_user(users)

        elif option == "nc":
            account_number = len(accounts) + 1
            account = create_account(BRANCH, account_number, users)

            if account:
                accounts.append(account)

        elif option == "lc":
            list_accounts(accounts)

        elif option == "q":
            break

        else:
            print("Invalid operation, please select the desired operation again.")


main()
