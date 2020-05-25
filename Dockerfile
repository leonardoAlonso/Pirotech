# pull official base image
FROM python:3.8.1-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APPLICATION_ENV 'DevelopmentConfig'

# update linux dependences
RUN apt-get update
RUN apt-get -y install python3-dev
RUN apt-get -y install build-essential
RUN apt-get -y install libpq-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/
