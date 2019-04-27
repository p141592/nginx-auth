FROM openresty/openresty

ENV openresty /usr/local/openresty

COPY src/nginx/nginx.nginx ${openresty}/nginx/conf/nginx.conf

COPY src/nginx/conf.d /etc/nginx/conf.d/

COPY src/vendor/ ${openresty}/lualib/
COPY src/lua ${openresty}/lualib/

EXPOSE 80