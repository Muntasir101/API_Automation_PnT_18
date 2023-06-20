import json
import string

import requests
from dotenv import dotenv_values
import os
import random

# Get the current file path
current_file_path = os.path.abspath(__file__)
# Get the root directory path
root_directory = os.path.dirname(current_file_path)
# Set the file path within the root directory
env_file_path = os.path.join(root_directory, '.env')

env_vars = dotenv_values(env_file_path)

api_token = env_vars['API_TOKEN']

base_url = "https://gorest.co.in"




