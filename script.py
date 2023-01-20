import requests
from os import path
from sys import exit
from json import load
from bs4 import BeautifulSoup
from webbrowser import open as wb_open


#Ensure config file exists
if not path.isdir("config"):
    print("Config folder does not exist. Please pull the latest stable branch.")
    exit(0)
config_filepath = path.join("config", "auth.json")
if not path.isfile(config_filepath):
    print(f"Auth file at {config_filepath} does not exist. Please pull the latest stable branch.")
    exit(0)

try:
    with open(config_filepath) as auth_file:
        creds = load(auth_file)
except IOError as e:
    print(f"Error reading file, {e.strerror}")
    exit(0)
except:
    print("Unknown error")
    exit(0)

if not "client_key" in creds.keys():
    print("Auth file is corrupted. Please pull the latest stable branch and re-enter credentials.")
    exit(0)


API_URL = "https://www.tiktok.com/auth/authorize/"
payload = {
    "client_key": creds["client_key"],
    "scope": "user.info.basic,video.list",
    "response_type": "code",
    "state": "1",           #TODO: Generate an actual random state
    "redirect_uri": "./"    #TODO: Link to an actual callback page
}
response = requests.get(API_URL, params = payload)
if response.status_code != 200:
    print(f"Response failed, recieved {response.status_code}")
login_page = BeautifulSoup(response.content, "html.parser")


try:
    #TODO: Integrate with Flask
    with open("index.html", "wt") as output_file:
        output_file.write(login_page.prettify())
except IOError as e:
    print(f"Error writing to file, {e.strerror}")
    exit(0)
except:
    print("Unknown error")
    exit(0)

wb_open("index.html")