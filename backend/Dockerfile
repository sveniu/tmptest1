FROM alpine:3.7
EXPOSE 80
VOLUME /usr/src/app/public
WORKDIR /usr/src/app
RUN apk add --no-cache \
        uwsgi-python \
        python
COPY . .
RUN rm -rf public/*
CMD [ "uwsgi", "--http-socket", "0.0.0.0:80", \
               "--plugins", "python", \
               "--processes", "8", \
               "--wsgi", "app:application" ]
