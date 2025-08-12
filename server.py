#!/usr/bin/env python

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

import os
import requests
import json
import dotenv

from dotenv import load_dotenv

load_dotenv()
your_auth0_domain = os.getenv("AUTH0_CLIENT_DOMAIN")
client_id         = os.getenv("AUTH0_API_CLIENT_ID")
client_secret     = os.getenv("AUTH0_M2M_SECRET")
audience_url      = os.getenv("AUTH0_AUDIENCE_URL")
return_url        = "http://127.0.0.1:8082/docs"

assert your_auth0_domain is not None, "Please set AUTH0_CLIENT_DOMAIN in your .env"
assert client_id is not None,          "Please set AUTH0_API_CLIENT_ID in your .env"
assert your_auth0_domain is not None,  "Please set AUTH0_M2M_SECRET in your .env"
assert your_auth0_domain is not None,  "Please set AUTH0_AUDIENCE_URL in your .env"


server = FastAPI()

@server.get("/login")
def login():
    return RedirectResponse(
        f"https://{your_auth0_domain}.us.auth0.com/authorize" +
        "?response_type=code" +
        f"&client_id={client_id}" +
        f"&redirect_uri={return_url}" +
        "&scope=offline_access" +  #  openid profile email
        f"&audience={audience_url}"
    )


@server.get("/token")
def get_access_token(code: str):
    payload = {
        "grant_type": "authorization_code",
        "client_id": client_id,
        "client_secret": client_secret,
        "code": code,
        "redirect_uri": return_url
    }

    headers = {"content-type":"application/x-www-form-urlencoded"}

    print(headers)
    print(payload)

    response = requests.post(
        f"https://{your_auth0_domain}.us.auth0.com/oauth/token", data=payload, headers=headers
        )
    print(json.dumps(response.json(),indent=4))

    return response.json()

