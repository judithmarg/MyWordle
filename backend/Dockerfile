FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pytest pytest-asyncio
COPY . /app

EXPOSE 8012
CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8012" ]
