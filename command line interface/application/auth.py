import requests

def saveApiToken(token) :
    file = open('application/apiToken/apiToken.txt','w')
    file.write(token)
    file.close()

def getApiToken() :
    file = open('application/apiToken/apiToken.txt','r')
    apiToken = file.readline()
    return apiToken

def verifyApiToken(token) :
    url = "http://127.0.0.1:8000/api/user"
    apiToken = token 
    headers = {'Authorization': f'Bearer {apiToken}'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200 :
        return True 
    else :
        return False 
    
def getUserData(token) :
    url = "http://127.0.0.1:8000/api/user"
    apiToken = token 
    headers = {'Authorization': f'Bearer {apiToken}'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200 :
        data = response.json()
        return data
    else :
        return False 

# Function to register and obtain API token
def register(name, email, password):

    url = "http://127.0.0.1:8000/api/register"
    body = {'name': name, 'email': email, 'password': password}

    response = requests.post(url, json=body)

    if response.status_code == 201:
        print("Registration successful!")
        data = response.json()
        apiToken = data['token']
        saveApiToken(apiToken)
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
        saveApiToken(apiToken)
        return apiToken
    else:
        print("Login failed")


