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

api_token = env_vars['API_TOKEN']

base_url = "https://gorest.co.in"


def get_all_user():
    url = base_url + "/public/v2/users"
    user_headers = {"Authorization": "Bearer " + api_token}
    response = requests.get(url, headers=user_headers)

    # verify status code
    try:
        assert response.status_code == 200
        print("GET Response Code Test passed.", response.status_code)
    except Exception as e:
        print("GET Response Code Exception arise.", type(e).__name__)

    # Get response body
    json_body = response.json()
    json_data = json.dumps(json_body, indent=4)
    print("Response Data: ", json_data)
    return json_data


get_all_user()
