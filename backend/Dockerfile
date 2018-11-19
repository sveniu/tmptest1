FROM alpine:3.7
EXPOSE 8080
VOLUME /usr/src/app/public
WORKDIR /usr/src/app
RUN apk add --no-cache \
        uwsgi-python \
        python
COPY . .
RUN rm -rf public/*
CMD [ "uwsgi", "--http-socket", "0.0.0.0:8080", \
               "--uid", "uwsgi", \
               "--plugins", "python", \
               "--wsgi", "app:application" ]
