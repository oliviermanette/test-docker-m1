FROM nginx:1.17-alpine

LABEL MAINTAINER="FirstName LastName <example@domain.com>"

RUN rm /etc/nginx/conf.d/default.conf
COPY conf.d/app.conf /etc/nginx/conf.d
COPY conf.d/timeout.conf /etc/nginx/conf.d
EXPOSE 80