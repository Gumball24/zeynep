FROM python:3.6-alpine

CMD ["monium", "run"]
VOLUME ["/data"]

COPY requirements.txt /

RUN pip install -r requirements.txt

COPY . /