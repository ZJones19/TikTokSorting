import requests
from os import path
from sys import exit
from json import load
from bs4 import BeautifulSoup


#Ensure config file exists
def get_config_filepath():
    if not path.isdir("config"):
        print("Config folder does not exist. Please pull the latest stable branch.")
        exit(0)
    config_filepath = path.join("config", "auth.json")
    if not path.isfile(config_filepath):
        print(f"Auth file at {config_filepath} does not exist. Please pull the latest stable branch.")
        exit(0)
    
    return config_filepath


def retrieve_key():
    config_filepath = get_config_filepath()
    try:
        with open(config_filepath) as auth_file:
            creds = load(auth_file)
    except IOError as e:
        print(f"Error reading config file")
        exit(0)
    except:
        print("Unknown error when attempting to read config file")
        exit(0)

    if not "client_key" in creds.keys():
        print("Auth file is corrupted. Please pull the latest stable branch and re-enter credentials.")
        exit(0)
    
    return creds["client_key"]


def generate_login_portal(redirect_uri):
    API_URL = "https://www.tiktok.com/auth/authorize/"
    payload = {
        "client_key": retrieve_key(),
        "scope": "user.info.basic,video.list",
        "response_type": "code",
        "state": "1"    #TODO: Generate an actual random state
    }
    payload["redirect_uri"] = redirect_uri

    response = requests.get(API_URL, params = payload)
    if response.status_code != 200:
        print(f"Response failed, recieved {response.status_code}")
    login_page = BeautifulSoup(response.content, "html.parser")

    return login_page.prettify("utf8")