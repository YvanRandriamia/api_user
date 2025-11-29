FROM python:latest

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements
COPY . .
EXPOSE 8080
CMD ["python", "app.py"]