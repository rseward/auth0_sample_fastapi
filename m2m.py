#!/usr/bin/env python

import os
import requests
import json
import dotenv

from dotenv import load_dotenv

import myjwt

load_dotenv()
your_auth0_domain = os.getenv("AUTH0_CLIENT_DOMAIN")


"""
Sample machine to machine authentication script to demonstrate the flow of
token using auth0.
"""

# copied from auth0 curl example.

payload = {
    "client_id": os.getenv("AUTH0_M2M_CLIENT_ID"),
    "client_secret": os.getenv("AUTH0_M2M_SECRET"),
    "audience": os.getenv("AUTH0_M2M_AUDIENCE"),
    "grant_type": "client_credentials"
}

print(payload)

response = requests.post(
    f"https://{your_auth0_domain}.us.auth0.com/oauth/token",
    json=payload
)
rjson = response.json()
print(rjson)

if "access_token" in rjson:
    # Decoding the JWT fails currently. :-(
    secret_key = os.getenv("AUTH0_M2M_SECRET")
    print(json.dumps(myjwt.decode_jwt(rjson["access_token"], secret_key=None),indent=4))


