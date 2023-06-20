from utils import *

current_file_path = os.path.abspath(__file__)
root_directory = os.path.dirname(current_file_path)
env_file_path = os.path.join(root_directory, '.env')
env_vars = dotenv_values(env_file_path)
api_token = env_vars['API_TOKEN']
base_url = env_vars['BASE_URL']


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

    # Get response body
    json_body = response.json()
    user_id = json_body["id"]

    return user_id


def put_user(id_user):
    url = base_url + f"/public/v2/users/{id_user}"
    print(url)
    user_headers = {"Authorization": "Bearer " + api_token}

    user_data = {
        "name": "name 1",
        "email": "email1@example.com",
        "gender": "male",
        "status": "active"
    }
    response = requests.put(url, json=user_data, headers=user_headers)

    assert response.status_code == 200
    print("PUT Response Code Test passed.", response.status_code)


id_update = new_user_id()
print(id_update)
put_user(id_update)
