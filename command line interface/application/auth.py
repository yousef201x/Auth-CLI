import requests

# Function to register and obtain API token
def register(name, email, password):

    url = "http://127.0.0.1:8000/api/register"
    body = {'name': name, 'email': email, 'password': password}

    response = requests.post(url, json=body)

    if response.status_code == 201:
        print("Registration successful!")
        data = response.json()
        apiToken = data['token']
        return apiToken
    else:
        print("Registration failed")
        data = response.json()
        errors = data['error']
        print(errors)

def login(email,password) :
    url = "http://127.0.0.1:8000/api/login"
    body = {'email': email, 'password': password}

    response = requests.post(url, json=body)

    print(response.status_code)

    if response.status_code == 200:
        print("Loged in successfully!")
        data = response.json()
        apiToken = data['token']
        username = data['username']
        print("Welcome ",username,"!")
        return apiToken
    else:
        print("Login failed")


