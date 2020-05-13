print("This program is copyright of Platinum Programming, Inc.")
print("The default password is 'pythonterminal'.")
print("Type 'help' for a list of commands.")
print("")


def command(data):
    inputCommand = input(data['username'] + "@pythonterminal:~ $ ")
    if inputCommand == "exit":
        quit()

    elif inputCommand == "print-data":
        print(" Your name is " + data['username'] + ".")

    elif inputCommand == "help":
        print(" The commands you can use are:")
        print("     exit - quit the terminal - This doesn't work in MU 1.0.2.")
        print("     help - opens the help page")
        print("     print-data - View your data")
        print("     change-user - Change the username")
        print("     change-password - Change the password")

    elif inputCommand == "":
        return False

    elif inputCommand == "change-user":
        print("Needs to be sudo. Try sudo change-user.")

    elif inputCommand == "change-password":
        print("Needs to be sudo. Try sudo change-password.")

    elif inputCommand == "sudo change-user":
        print("This command requires superuser privileges.")
        inputPassword = input("What is your password? ")
        if inputPassword == data['password']:
            check = True
        else:
            check = False
        if check == True:
            result = data
            result['username'] = input("What would you like the username to be? ")
            origUser = False
            return result
        else:
            print("Sorry, the password is incorrect.")

    elif inputCommand == "sudo change-password":
        print("This command requres superuser privileges.")
        inputPassword = input("What is your password? ")
        if inputPassword == data['password']:
            check = True
        else:
            check = False
        if check == True:
            result = data
            result['password'] = input("What would you like the password to be? ")
            origPassword = False
            return result
        else:
            print("Sorry, the password is incorrect.")

    else:
        print(" Bash: " + inputCommand + ": command not found.")
    return False


data = {
    'username': 'terminal',
    'password': 'pythonterminal'
}
while True:
    changes = command(data)
    if changes:
        data = changes
