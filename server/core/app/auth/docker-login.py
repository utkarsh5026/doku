import requests
import os

# import the dokcerhub variable from the settings file
from django.conf import settings

auth_url = f"{settings.DOCKER_HUB_URL}/users/login/"

def send_auth_credentials_to_docker(username: str, password: str):
    response = requests.post(auth_url, json={"username": username, "password": password})
    
    print(response.json())
    
    
    
if __name__ == "__main__":
    send_auth_credentials_to_docker("uk5026", "@Overkill35026")
