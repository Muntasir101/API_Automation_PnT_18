import json
import requests
from dotenv import dotenv_values
import os


# Get the current file path
current_file_path = os.path.abspath(__file__)
# Get the root directory path
root_directory = os.path.dirname(current_file_path)
# Set the file path within the root directory
env_file_path = os.path.join(root_directory, '.env')


env_vars = dotenv_values(env_file_path)

db_username = env_vars['DB_USERNAME']
print(db_username)

#..............
import json

import requests
from dotenv import dotenv_values
import os
from POST_user import post_user, new_user_id

current_file_path = os.path.abspath(__file__)
root_directory = os.path.dirname(current_file_path)
env_file_path = os.path.join(root_directory, '.env')
env_vars = dotenv_values(env_file_path)
api_token = env_vars['API_TOKEN']
base_url = env_vars['BASE_URL']


def put_user(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    user_headers = {"Authorization": "Bearer " + api_token}

    user_data = {
        "name": "name 1",
        "email": "email1@example.com",
        "gender": 'male',
        "status": 'active'
    }
    response = requests.put(url, json=user_data, headers=user_headers)

    try:
        assert response.status_code == 200
        print("PUT Response Code Test passed.", response.status_code)
        # Get response body
        json_body = response.json()
        json_data = json.dumps(json_body, indent=4)
        print("Response Data: ", json_data)

        """
        assert json_body['id'] == user_id
        assert json_body['name'] == user_data['name']
        assert json_body['email'] == user_data['email']
        assert json_body['gender'] == user_data['gender']
        assert json_body['status'] == user_data['status']
        """
    except Exception as e:
        print("PUT Response Code Exception arise.", type(e).__name__)


put_user(new_user_id())