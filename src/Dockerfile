FROM python:3.10-alpine

WORKDIR /usr/src/app
RUN pip install --upgrade pip
RUN apk add --update --no-cache build-base \
    libffi-dev openssl-dev bash git gcc sqlite \
    curl pwgen mysql-client

COPY . /usr/src/app/givemeadatabase/
WORKDIR /usr/src/app/givemeadatabase/

RUN pip install -r requirements.txt
RUN pip install uwsgi
RUN export FLASK_APP=givemeadatabase;
ENV PYTHONUNBUFFERED=1
EXPOSE 80
ENTRYPOINT [ "./entrypoint.sh" ]
