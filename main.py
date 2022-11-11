import requests
from datetime import datetime

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

# create_graph_response = requests.post(url=pixela_endpoint_create_graph, json=create_graph_params, headers=headers)
# print(create_graph_response.text)
#CHECK OUT THE GRAPH BY GOING HERE: "https://pixe.la/v1/users/fatemakotha/graphs/graph1.html"

#..............................................................................................................................................................
GRAPH_ID = "graph1"
pixela_endpoint_add_to_graph = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.today()
print(today) #2022-11-11 16:38:15.214336

today_format_changed = today.strftime("%Y%m%d")
print(today_format_changed) #20221111



add_to_graph_params = {
    "date": "20221111",
    "quantity": "7",
}

# add_input_to_graph = requests.post(url=pixela_endpoint_add_to_graph, json=add_to_graph_params, headers=headers)
# print(add_input_to_graph.text) #prints: {"message":"Success.","isSuccess":true}
#CHECK IT PUT HERE: https://pixe.la/v1/users/fatemakotha/graphs/graph1.html

#...............................................................................................................................
