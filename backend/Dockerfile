FROM python:3.9

WORKDIR /backend

ENV FLASK_APP=server

ENV PYTHONPATH="${PYTHONPATH}:/backend"

RUN pip install --upgrade pip

RUN apt-get -q update && apt-get -qy install netcat

RUN curl -OL https://raw.githubusercontent.com/mrako/wait-for/master/wait-for && chmod +x wait-for

COPY . /backend/

RUN pip install -r requirements.txt

EXPOSE 5000
