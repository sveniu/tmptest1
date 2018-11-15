FROM alpine:3.7
EXPOSE 3031
VOLUME /usr/src/app/public
WORKDIR /usr/src/app
RUN apk add --no-cache \
        uwsgi-python \
        python
COPY . .
RUN envsubst < local.env.tpl > local.env
RUN rm -rf public/*
CMD [ "uwsgi", "--http-socket", "0.0.0.0:3031", \
               "--uid", "uwsgi", \
               "--plugins", "python", \
               "--wsgi", "app:application" ]
