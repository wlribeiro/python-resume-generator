install:
	pip install -r requirements.txt

run:
	cd src/ && uvicorn api:app --reload

clear-pdf:
	rm src/public/pdf/*.pdf