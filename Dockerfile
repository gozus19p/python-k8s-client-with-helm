FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt
COPY src src

RUN pip install -r requirements.txt

ENV FLASK_APP=app.py

WORKDIR /app/src/main/python

ENTRYPOINT ["python", "-m", "flask", "run", "--host=0.0.0.0"]