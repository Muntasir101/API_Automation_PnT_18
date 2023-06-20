import json
import requests
from dotenv import dotenv_values
import os
from utils import *

# Get the current file path
current_file_path = os.path.abspath(__file__)
# Get the root directory path
root_directory = os.path.dirname(current_file_path)
# Set the file path within the root directory
env_file_path = os.path.join(root_directory, '.env')

env_vars = dotenv_values(env_file_path)

api_token = env_vars['API_TOKEN']
base_url = env_vars['BASE_URL']


def post_user():
    url = base_url + "/public/v2/users"
    user_headers = {"Authorization": "Bearer " + api_token}
    # payload
    user_data = {
        "name": random_name(),
        "email": random_email(),
        "gender": random_gender(),
        "status": random_status()
    }
    response = requests.post(url, json=user_data, headers=user_headers)

    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)

    assert response.status_code == 201
    print("POST Response Code Test passed.", response.status_code)

    # Get response body
    json_body = response.json()
    json_data = json.dumps(json_body, indent=4)
    print("Response Data: ", json_data)

"""
# it works
for _ in range(10):
    user_email = random_email()
    user_name = random_name()
    user_gender = random_gender()
    user_status = random_status()
    post_user(user_email, user_name, user_gender, user_status)
    print(f"{user_name} {user_email} {user_gender} {user_status}")
"""
post_user()




