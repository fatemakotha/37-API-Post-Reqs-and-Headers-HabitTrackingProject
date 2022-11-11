import requests

USERNAME = "fatemakotha"
TOKEN = "jh5jh5jh5jjh5jh5"
pixela_endpoint = "https://pixe.la/v1/users"


user_params = {
    "token": "jh5jh5jh5jjh5jh5", #set yourself
    "username": "fatemakotha", #set yourself
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
#Create a new user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text) #PRINTS: {"message":"Success. Let's visit https://pixe.la/@fatemakotha , it is your profile page!","isSuccess":true}

#..........................................................................................................................................................

pixela_endpoint_create_graph = f"{pixela_endpoint}/{USERNAME}/graphs"
create_graph_params = {
    "id": "graph1",
    "name": "Commitment Graph",
    "unit": "Commit",
    "type": "int",
    "color": "kuro",
}

headers = {
    "X-USER-TOKEN": "jh5jh5jh5jjh5jh5",
}

create_graph_response = requests.post(url=pixela_endpoint_create_graph, json=create_graph_params, headers=headers)
print(create_graph_response.text)
