FROM openresty/openresty

ENV openresty /usr/local/openresty/

COPY ./src/nginx/nginx.conf ${openresty}nginx/conf/nginx.conf
COPY ./src/nginx/global.conf /etc/nginx/
COPY ./src/nginx/http.conf /etc/nginx/


COPY ./src/nginx/conf.d/ /etc/nginx/conf.d/

COPY ./src/lua/ ${openresty}lualib/

EXPOSE 8000:80