FROM python:3.7.4-buster
WORKDIR /app
COPY requirements.txt .
COPY ./src ./src
RUN pip install -r requirements.txt
CMD ["python", "./src/app.py"]
EXPOSE 5000