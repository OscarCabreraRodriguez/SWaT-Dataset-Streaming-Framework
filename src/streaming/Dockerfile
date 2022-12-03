FROM python:3.8-slim-buster

RUN apt-get update
RUN apt-get install nano

RUN mkdir wd
WORKDIR wd
COPY plotly_app/requirements.txt .
RUN pip3 install -r requirements.txt

COPY plotly_app/ ./

CMD [ "gunicorn", "--workers=1", "--threads=1", "-b 0.0.0.0:80", "app:server"]