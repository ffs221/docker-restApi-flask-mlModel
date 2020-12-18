FROM python:3.7.3-stretch
ENV PYTHONBUFFERED 1
ENV PYTHON_VERSION 3.7.3
RUN mkdir -p /server
WORKDIR /server

COPY . /server

RUN ["pip3", "install", "pipenv"]

RUN ["pipenv", "install"]

CMD pipenv run flask run --host 0.0.0.0 --port 5000

