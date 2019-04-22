FROM openresty/openresty

VOLUME ./src/nginx/:/etc/nginx/

EXPOSE 8000:80