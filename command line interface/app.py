import application.auth as auth

# Global variable to store API token
apiToken = auth.getApiToken()

if not auth.verifyApiToken(apiToken) or len(apiToken) == 0 :
    while True:
        print("\nWelcome to the CLI:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        action = input("Select an option: ")

        if action == "1":
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            response = auth.register(name,email,password)
            if response != 'Registration failed' :
                apiToken = response
            elif action == "2":
                email = input("Enter your email: ")
                password = input("Enter your password: ")
                response = auth.login(email,password)
                if response != 'Registration failed' :
                    apiToken = response
            elif action == "3":
                print("Exiting the program.")
                break
            else:
                print("Invalid input. Please choose a valid option.")
        else:
            userInfo = auth.getUserData(apiToken)
            print("welcome back ",userInfo['name'],' !')
            action = input("enter name")
else :
    userInfo = auth.getUserData(apiToken)
    print("\nwelcome back ",userInfo['name'],' !')
    while True:
        print("1.")
        print("2.")
        print("3. Logout")

