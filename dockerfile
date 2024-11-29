FROM python:3.9-slim AS base

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt 

COPY . .

FROM python:3.9-slim

WORKDIR /app

COPY --from=base /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

COPY --from=base /app /app

RUN ls -la /app

EXPOSE 8080

CMD ["python","main.py"]