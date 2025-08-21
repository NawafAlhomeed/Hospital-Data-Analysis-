.PHONY: install test run

install:
	python -m venv .venv
	. .venv/bin/activate && pip install -r requirements.txt

test:
	. .venv/bin/activate && pip install -r requirements-dev.txt && pytest -q

run:
	python -m hospital_etl.cli data/raw data/processed
