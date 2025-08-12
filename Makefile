deps:	.venv
	uv pip install -r requirements.txt


.venv:
	uv venv

run:	.venv
	.venv/bin/uvicorn server:server --port 8082 --reload
	#uvicorn main:app --port 8080 --reload