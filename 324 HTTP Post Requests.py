# Types of HTTP Requests:
# GET: requests.get() is made where we ask an external system for a particular piece of data in the form of response
# POST: requests.post() is where we give the ext system some piece of data & we are not interested in the response other than whether it was successful
# PUT: requests.put() is where we update a piece of data in the ext service i.e. lets say you want to update sth in a spreadcheet
# DELETE: requests.delete() is where we delete a piece of data from ext ervice i.e. delete a fb post

import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "jh5jh5jh5jjh5jh5", #set yourself
    "username": "fatemakotha", #set yourself
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
#Create a new user in pixela
response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text) #PRINTS: {"message":"Success. Let's visit https://pixe.la/@fatemakotha , it is your profile page!","isSuccess":true}