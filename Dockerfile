FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p pictures

EXPOSE 5000

ENV DB_PATH=/app/data/libo.db

CMD ["python", "run.py"]
