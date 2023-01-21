from flask import Flask
from src.login import generate_login_portal as login_portal


app = Flask(__name__)
@app.route("/")
def main():
    return login_portal("https://http://127.0.0.1:5000/")