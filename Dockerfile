FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt requirements-dev.txt /app/
RUN python -m pip install --upgrade pip &&             pip install --no-cache-dir -r requirements.txt

COPY src/ /app/src/
WORKDIR /app
ENV PYTHONPATH=/app/src
CMD ["python", "-m", "hospital_etl.cli", "data/raw", "data/processed"]
