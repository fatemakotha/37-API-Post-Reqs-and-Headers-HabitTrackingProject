import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "jh5jh5jh5jjh5jh5", #set yourself
    "username": "fatemakotha", #set yourself
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
#Create a new user
response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text) #PRINTS: {"message":"Success. Let's visit https://pixe.la/@fatemakotha , it is your profile page!","isSuccess":true}