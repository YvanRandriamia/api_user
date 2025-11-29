FROM python:latest

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements
COPY . .
EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]