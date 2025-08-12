deps:
	uv pip install -r requirements.txt


run:
	uvicorn server:server --port 8082 --reload
	#uvicorn main:app --port 8080 --reload