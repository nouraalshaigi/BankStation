def ask_name():
    return input("Enter your name: ")

def ask_id():
    return input("Enter your ID: ")

def ask_new_account_balance():
    return float(input("Enter your new account balance: "))

def main():
    while True:
        action = input("A new client? (yes/no): ")
        if action.lower() == "yes":
            name = ask_name()
            id = ask_id()
            print("Name: ", name)
            print("ID: ", id)
        elif action.lower() == "no":
            balance = ask_new_account_balance()
            print("New account balance: ", balance)
        else:
            print("Invalid input, please try again.")
        continue_input = input("Do you want to continue? (yes/no): ")
        if continue_input.lower() == "no":
            break

if __name__ == "__main__":
    main()