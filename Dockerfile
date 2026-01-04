FROM python:3.13-slim

WORKDIR /api
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app ./app
COPY main.py .

CMD ["python", "main.py"]