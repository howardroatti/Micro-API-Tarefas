.PHONY: install run test format

install:
	pip install -r requirements.txt

run:
	uvicorn app.main:app --reload

test:
	pytest tests/ -v

format:
	black .
