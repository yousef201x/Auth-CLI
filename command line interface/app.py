import application.auth as auth
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

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
                print(Fore.MAGENTA + "Enter 'back' at any time to return to the main menu.")
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
                print(Fore.MAGENTA + "Enter 'back' at any time to return to the main menu.")
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
        print("\n" + Fore.GREEN + "Welcome back", userInfo['name'], '!')
        while True:
            print("1.")
            print("2.")
            print(Fore.RED + "3. Logout")

            action = input(Style.RESET_ALL + "Select an option: ")

            if action == "1" :
                # Your code for option 1
                pass
            elif action == "2" :
                # Your code for option 2
                pass
            elif action == "3" :
                response = auth.logout(apiToken)
                break
