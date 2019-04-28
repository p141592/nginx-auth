FROM openresty/openresty

ENV openresty /usr/local/openresty

COPY ssl/nginx-auth.key /etc/ssl/certs/nginx-auth.key
COPY ssl/nginx-auth.crt /etc/ssl/private/nginx-auth.crt
COPY ssl/nginx-auth.pem /etc/ssl/certs/nginx-auth.pem

COPY src/nginx/nginx.nginx ${openresty}/nginx/conf/nginx.conf
COPY src/nginx/ssl.nginx ${openresty}/nginx/conf/ssl.nginx
COPY src/nginx/proxy_params.nginx ${openresty}/nginx/conf/proxy_params

COPY src/nginx/conf.d /etc/nginx/conf.d/

COPY src/vendor/ ${openresty}/lualib/
COPY src/lua ${openresty}/lualib/

EXPOSE 80