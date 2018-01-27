FROM python:3.6-alpine
MAINTAINER fp.flyingpi@gmail.com
ENV PYTHONUNBUFFERED 1
RUN apk --update add postgresql-dev alpine-sdk
RUN mkdir /backend_fdlb
WORKDIR /backend_fdlb
ADD requirements.txt /backend_fdlb/requirements.txt
RUN pip install -r requirements.txt
ADD . /backend_fdlb