# Project

Simple project to illustrate how to integrate auth0 into a python fastapi end point.

To follow allong you will need to create a auth0 account to exercise this code.

You will need to create a version of the .env file for the project that includes all
the necessary vars set for integration with your auth0 account.

## Source

Please see these microapis youtube channel videos for more information especially about configuring your auth0 account:

- https://www.youtube.com/watch?v=PbUcQUQ7K2o&t
- https://www.youtube.com/watch?v=ato2S5b27o8

## Auth0 Account

You will want to visit your Auth0 dashboard to obtain / specify your Auth0 configuration information for this demonstration,

- Auth0 Dashboard: https://manage.auth0.com/

Once you have obtained the information. 

1) Copy .env.template to .env
2) Uncomment the variables in the .env file and populate with appropriate
   values from your account.

## How To Execute

1) Create Auth0 Account and applications.
2) Populate your .env file for this demo
3) Build the python environment. Use make and the uv build tool if you have them.

```
make deps
```

3) Run the m2m.py test.

```
uv run m2m.py
```

If m2m.py succeeds you should see a JWT sent back by Auth0

4) Run the server.py test

```
.venv/bin/uvicorn uvicorn server:server --port 8082 --reload
```

5) Use a browser to visit your api end point to login.

http://127.0.0.1:8082/login

6) If your Auth0 login was successful. Copy the returned code in the /doc URL
   into the FastAPI swagger interface for the /token code end point. Watch the 
   microapis youtube videos for more information.

If your FastAPI Swagger /token test is successful, you should see your JWT obtained
from auth0.
