FROM python:3.11-slim-buster

WORKDIR /app

COPY /s1 /app/s1
COPY /s2 /app/s2
COPY main.py .
COPY requc.txt .

RUN pip install --no-cache-dir -r requc.txt

EXPOSE 2456

CMD ["python3", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--reload", "--port", "2456"]
