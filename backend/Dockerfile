FROM python:3.9

WORKDIR /backend

ENV FLASK_APP=server

ENV PYTHONPATH="${PYTHONPATH}:/backend"

RUN pip install --upgrade pip

COPY . /backend/

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["flask", "db", "upgrade"]

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]
