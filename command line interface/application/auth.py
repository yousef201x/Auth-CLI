import requests

# Function to save the API token to a text file
def saveApiToken(token):
    file = open('application/apiToken/apiToken.txt', 'w')  # Open file in write mode
    file.write(token)  # Write the token to the file
    file.close()  # Close the file

# Function to read the API token from the text file
def getApiToken():
    file = open('application/apiToken/apiToken.txt', 'r')  # Open file in read mode
    apiToken = file.readline()  # Read the token from the file
    return apiToken  # Return the token

# Function to verify if the API token is valid by making a request to a URL
def verifyApiToken(token):
    url = "http://127.0.0.1:8000/api/user"  # URL to check the token
    apiToken = token  # Assign token to variable
    headers = {'Authorization': f'Bearer {apiToken}'}  # Set authorization header

    response = requests.get(url, headers=headers)  # Send GET request with token

    if response.status_code == 200:
        return True  # Token is valid
    else:
        return False  # Token is invalid
    
def clearApiTokenFile() :
    with open('application/apiToken/apiToken.txt', 'w') as file:
        file.truncate(0)

# Function to get user data using the API token
def getUserData(token):
    url = "http://127.0.0.1:8000/api/user"  # URL to fetch user data
    apiToken = token  # Assign token to variable
    headers = {'Authorization': f'Bearer {apiToken}'}  # Set authorization header

    response = requests.get(url, headers=headers)  # Send GET request with token

    if response.status_code == 200:
        data = response.json()  # Parse JSON response
        return data  # Return user data
    else:
        return False  # Failed to fetch user data

# Function to register a user and obtain an API token
def register(name, email, password):
    url = "http://127.0.0.1:8000/api/register"  # Registration API endpoint
    body = {'name': name, 'email': email, 'password': password}  # Request body

    response = requests.post(url, json=body)  # Send POST request with registration data

    if response.status_code == 201:  # Successful registration
        print("Registration successful!")
        data = response.json()  # Parse JSON response
        apiToken = data['token']  # Extract API token from response
        saveApiToken(apiToken)  # Save API token to file
        return apiToken  # Return API token
    else:  # Registration failed
        print("Registration failed")
        data = response.json()  # Parse JSON response
        errors = data['error']  # Extract error message from response
        print(errors)  # Print error message

# Function to log in a user and obtain an API token
def login(email, password):
    url = "http://127.0.0.1:8000/api/login"  # Login API endpoint
    body = {'email': email, 'password': password}  # Request body

    response = requests.post(url, json=body)  # Send POST request with login data

    if response.status_code == 200:  # Successful login
        print("Logged in successfully!")
        data = response.json()  # Parse JSON response
        apiToken = data['token']  # Extract API token from response
        username = data['username']  # Extract username from response
        print("Welcome ", username, "!")  # Print welcome message
        saveApiToken(apiToken)  # Save API token to file
        return apiToken  # Return API token
    else:  # Login failed
        print("Login failed")

def logout(token) :
    url = "http://127.0.0.1:8000/api/logout" 
    apiToken = token  # Assign token to variable
    headers = {'Authorization': f'Bearer {apiToken}'}  # Set authorization header

    response = requests.post(url, headers=headers)  # Send GET request with token

    if response.status_code == 200:
        clearApiTokenFile()
        return True
    else:
        return False 

