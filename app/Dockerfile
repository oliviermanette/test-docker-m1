FROM python:3.6.8-alpine3.9

LABEL MAINTAINER="FirstName LastName <example@domain.com>"

ENV GROUP_ID=1000 \
    USER_ID=1000

WORKDIR /var/www/

ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

ADD ./requirements.txt /var/www/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ADD . /var/www/
RUN pip install gunicorn

RUN addgroup -g $GROUP_ID www
RUN adduser -D -u $USER_ID -G www www -s /bin/sh

USER www

EXPOSE 5000

CMD [ "gunicorn", "--timeout" , "2000" , "-w", "4", "--bind", "0.0.0.0:5000", "wsgi", "--reload" ,"--log-level", "debug" ]