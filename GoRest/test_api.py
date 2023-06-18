import json
import requests
from dotenv import dotenv_values
import os


# Get the current file path
current_file_path = os.path.abspath(__file__)
# Get the root directory path
root_directory = os.path.dirname(current_file_path)
# Set the file path within the root directory
file_path = os.path.join(root_directory, '.env')


env_vars = dotenv_values(file_path)

api_token = env_vars['API_TOKEN']

base_url = "https://gorest.co.in"


def get_all_user():
    url = base_url + "/public/v2/users"
    user_headers = {"Authorization": "Bearer " + api_token}
    response = requests.get(url, headers=user_headers)

    # verify status code
    try:
        assert response.status_code == 200
        print("Response Code Test passed.", response.status_code)
    except Exception as e:
        print("Response Code Exception arise.", type(e).__name__)

    # Get response body
    json_body = response.json()
    json_data = json.dumps(json_body, indent=4)
    print("Response Data: ", json_data)


# get_all_user()


def post_user(unique_email):
    url = base_url + "/public/v2/users"
    user_headers = {"Authorization": "Bearer " + api_token}
    # payload
    user_data = {
        "name": "Ironman",
        "email": unique_email,
        "gender": "male",
        "status": "active"
    }
    response = requests.post(url, json=user_data, headers=user_headers)

    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)

    # user_id = json_data["id"]
    # print("User ID: ", user_id)

    # verify status code
    try:
        assert response.status_code == 201
        print("Response Code Test passed.", response.status_code)

    except Exception as e:
        print("Response Code Exception arise.", type(e).__name__)
        assert json_data["message"] == "has already been taken"


post_user("mail2e333@gmail.com")
