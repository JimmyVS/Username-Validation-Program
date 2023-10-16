# This program has been created by Jimgr1. 
# Please do not publish the code and do not claim it as yours.
# To run this program you need to have installed python.
# Have fun coding!


def UsernameCheck():

    passed = 0  # This variable tracks whether the username validation has passed (1) or not (0).

    symbols = ["`", "~", "!", "@", "#", "$", "%", "^", "&",
               "*", "(", ")", "-", "_", "+", "=", "{", "}",
               "[", "]", ":", ";", '"', "'", ",", "<", ".",
               ">", "?", "/"]  # List of forbidden symbols in the username.

    # Continue validation until 'passed' becomes 1 (i.e., a valid username is entered).
    while passed == 0:

        lengthCheck = 1  # Initialize the length check flag to 1.
        symbolsCheck = 1  # Initialize the symbols check flag to 1.
        emptyCheck = 1  # Initialize the empty check flag to 1.
        spaceCheck = 1  # Initialize the space check flag to 1.

        spaceCounter = 0  # Initialize a counter for spaces in the username.
        symbolsCounter = 0  # Initialize a counter for forbidden symbols in the username.

        # Prompt the user to enter a username.
        username = input("Write a simple username: ")  
        print("")

        if len(username) > 8:
            print("Username must be shorter than 8 characters.")
            print("Try again.")
            print("")

            lengthCheck = 0  # Username length check failed.

        if len(username) <= 2:
            print("Username must be longer than 2 characters.")
            print("Try again.")
            print("")

            lengthCheck = 0  # Username length check failed.

        if len(username) > 2 and len(username) <= 8:
            lengthCheck = 1  # Username length check passed.

        if username.isspace():
            print("Username must contain characters.")
            print("Try again.")
            print("")

            emptyCheck = 0  # Username empty check failed.

        for i in range(len(username)):

            if symbols.__contains__(username[i]):
                print("Username with characters (!, @, #...) is invalid.")
                print("Try again.")
                print("")

                symbolsCounter += 1  # Count forbidden symbols found in the username.

            if username[i].isspace():
                spaceCounter += 1  # Count spaces found in the username.

        if symbolsCounter > 0:
            symbolsCheck = 0  # Username symbols check failed.

        else:
            symbolsCheck = 1  # Username symbols check passed.

        if spaceCounter > 0:
            print("Username must not contain spaces.")
            print("Try again.")
            print("")

            spaceCheck = 0  # Username space check failed.

        else:
            spaceCheck = 1  # Username space check passed.


        # Checks if all the flags are equal to 1.
        if lengthCheck == 1 and symbolsCheck == 1 and emptyCheck == 1 and spaceCheck == 1:

            print("Valid username.")

            passed = 1  # Set 'passed' to 1, indicating a valid username.

            # Prints the valid username.
            print("Your username is: '", end = username + "'")
            print(" Remember it.")

