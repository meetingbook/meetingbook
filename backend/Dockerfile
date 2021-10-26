FROM python:3.9

WORKDIR /backend

ENV FLASK_APP=server

ENV PYTHONPATH="${PYTHONPATH}:/backend"

RUN pip install --upgrade pip

RUN apt-get -q update && apt-get -qy install netcat

COPY . /backend/

RUN pip install -r requirements.txt

EXPOSE 5000
