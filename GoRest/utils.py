import os
import random
import string
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





