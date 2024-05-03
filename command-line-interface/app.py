import application.auth as auth
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Back message
def backAble() :
    return print(Fore.RED + "Enter 'back' at any time to return to the main menu.")

# Global variable to store API token
apiToken = auth.getApiToken()  # Retrieve API token from the saved file

while True:
    # Check if the API token is valid or empty
    if not auth.verifyApiToken(apiToken) or len(apiToken) == 0:
        print("\n" + Fore.YELLOW + "Welcome to the CLI:")
        print("1. " + Fore.GREEN + "Register")
        print("2. " + Fore.CYAN + "Login")
        print("3. " + Fore.RED + "Exit")

        action = input(Style.RESET_ALL + "Select an option: ")

        if action == "1":  # Register a new user
            while True:
                print("\n" + Fore.GREEN + "Register:")
                # Display back message
                backAble()
                name = input("Enter your name: ")
                if name.lower() == "back":
                    break
                email = input("Enter your email: ")
                if email.lower() == "back":
                    break
                password = input("Enter your password: ")
                if password.lower() == "back":
                    break
                response = auth.register(name, email, password)  # Call register function
                if response != 'Registration failed':  # Check if registration was successful
                    apiToken = response  # Update API token with the new token
                    break  # Exit the registration loop
        elif action == "2":  # Login if registration failed
            while True:
                print("\n" + Fore.CYAN + "Login:")
                # Display back message
                backAble()
                email = input("Enter your email: ")
                if email.lower() == "back":
                    break
                password = input("Enter your password: ")
                if password.lower() == "back":
                    break
                response = auth.login(email, password)  # Call login function
                if response != 'Login failed':  # Check if login was successful
                    apiToken = response  # Update API token with the new token
                    break  # Exit the login loop
        elif action == "3":  # Exit the program
            print(Fore.RED + "Exiting the program.")
            break
        else:
            print(Fore.RED + "Invalid input. Please choose a valid option.")

    else:  # User is already authenticated
        userInfo = auth.getUserData(apiToken)  # Get user data using the API token
        print("\n" + Fore.GREEN + "Welcome back", userInfo['name'], '!') # Dispaly welcome message
        while True: # Main menu
            print("1. " + Fore.CYAN + "My profile")
            print("2. "+Fore.RED + "Logout")

            action = input(Style.RESET_ALL + "Select an option: ") # Option inout

            if action == "1" :
                while True : # Display user info
                    print("\n" + Fore.YELLOW + "Welcome to My profile:")
                    backAble()
                    print("1. " + Fore.GREEN + "Name :" + userInfo['name'])
                    print("2. " + Fore.GREEN + "Email : " +userInfo['email'])
                    print("2. " + Fore.GREEN + "Account created at : " +userInfo['created_at'])
                    
                    action = input("Enter 'back' to go back: ")
                    if action.lower() == 'back' :
                        break
            elif action == "2" :
                response = auth.logout(apiToken)
                break
