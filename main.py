import requests
from datetime import datetime

USERNAME = "sehgal"
TOKEN = "abcdef1234"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
#print(response.text)

habit_endpoint = f"{graph_endpoint}/graph1"

today = datetime.now()

habit_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many km did you cycled today?"),
}

response = requests.post(url=habit_endpoint, json=habit_params, headers=headers)
print(response.text)


