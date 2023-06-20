import json
import os
import random
import string
import json
import requests
from dotenv import dotenv_values

import requests

# Get the current file path
current_file_path = os.path.abspath(__file__)
# Get the root directory path
root_directory = os.path.dirname(current_file_path)
# Set the file path within the root directory
env_file_path = os.path.join(root_directory, '.env')

env_vars = dotenv_values(env_file_path)

api_token = env_vars['API_TOKEN']
base_url = env_vars['BASE_URL']


def random_email():
    domain = ['gmail.com', 'yahoo.com', 'outlook.com']
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(7))
    random_domain = random.choice(domain)
    email = f"{random_string}@{random_domain}"
    return email


def random_name():
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(7))
    return random_string


def random_gender():
    gender_type = ['male', 'female']
    gender = random.choice(gender_type)
    return gender


def random_status():
    status_type = ['active', 'inactive']
    status = random.choice(status_type)
    return status


def new_user_id():
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

    # Get response body
    json_body = response.json()
    json_data = json.dumps(json_body, indent=4)

    user_id = json_body["id"]

    return user_id


print(new_user_id())
