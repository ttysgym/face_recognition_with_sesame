# -*- coding: utf-8 -*-
import requests
import json
import binascii
import time
from threading import Thread, Timer

def init():
    # login CANDY HOUSE account and get token
    url = "https://api.candyhouse.co/v1/accounts/login"
    head = {"Content-type": "application/json"}
    # Edit your email and password for CANDY HOUSE dashboard
    payload = {"email":"xxxxxxxx", "password":"xxxxxx"}
    response = requests.post(url, headers=head, data=json.dumps(payload))
    token = response.json()["authorization"]
    return token

def callAPI(token):
    headers = {"X-Authorization":token,}
    # Edut your secret key into the URL
    response = requests.get("https://api.candyhouse.co/v1/sesames/xxxxxx", headers=headers)
    status = response.json()["is_unlocked"]
    # Edut your secret key into the URL
    url_control = "https://api.candyhouse.co/v1/sesames/xxxxxx/control"
    head_control = {"X-Authorization": token, "Content-type": "application/json"}

    if status:
        payload_control = {"type":"lock"}
    else:
        payload_control = {"type":"unlock"}

    response_control = requests.post(url_control, headers=head_control, data=json.dumps(payload_control))
    print(response_control.text)
