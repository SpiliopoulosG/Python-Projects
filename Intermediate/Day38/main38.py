from datetime import *
import requests

USERNAME = "spiliopoulosg"
TOKEN = "ak/sd.f/[[sdf]ifd;fdf!@$fs&)fs$!"

pixela_endpoint = "https://pixe.la/v1/users"

# user_param = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
#
# response = requests.post(url=pixela_endpoint, json=user_param)
# print(response.text)


# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config = {
#     "id": "graph1",
#     "name": "Coding Challenge",
#     "unit": "Days",
#     "type": "int",
#     "color": "ajisai"
# }
#
headers = {
    "X-USER-TOKEN": TOKEN
}

today = datetime.now()
print(today.strftime("%Y%m%d"))

# graph_add_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
#
# pixel_config = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": "1"
# }
#
# response = requests.post(url=graph_add_endpoint, json=pixel_config, headers=headers)
# print(response.text)


# graph_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"
#
# pixel_config = {
#     "quantity": "15"
# }
#
# response = requests.put(url=graph_update_endpoint, json=pixel_config, headers=headers)
# print(response.text)

# graph_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"
#
#
#
# response = requests.put(url=graph_delete_endpoint, headers=headers)
# print(response.text)