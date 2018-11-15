FROM nginx:alpine
COPY index.html script.js style.css /usr/share/nginx/html/
RUN envsubst < /usr/share/nginx/html/index.html > /usr/share/nginx/html/index.html.new && mv -f /usr/share/nginx/html/index.html.new /usr/share/nginx/html/index.html
