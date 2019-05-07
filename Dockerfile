FROM alpine:3.9.3
ENV RESTY_OPENSSL_VERSION=1.1.0j
ENV RESTY_PCRE_VERSION=8.42
ENV RESTY_VERSION=1.13.6.2

ARG RESTY_CONFIG_OPTIONS="\
    --with-openssl=/tmp/openssl-${RESTY_OPENSSL_VERSION} \
    --with-pcre=/tmp/pcre-${RESTY_PCRE_VERSION} \
    --with-file-aio \
    --with-http_addition_module \
    --with-http_auth_request_module \
    --with-http_dav_module \
    --with-http_flv_module \
    --with-http_geoip_module=dynamic \
    --with-http_gunzip_module \
    --with-http_gzip_static_module \
    --with-http_image_filter_module=dynamic \
    --with-http_mp4_module \
    --with-http_random_index_module \
    --with-http_realip_module \
    --with-http_secure_link_module \
    --with-http_slice_module \
    --with-http_ssl_module \
    --with-http_stub_status_module \
    --with-http_sub_module \
    --with-http_v2_module \
    --with-http_xslt_module=dynamic \
    --with-ipv6 \
    --with-mail \
    --with-mail_ssl_module \
    --with-md5-asm \
    --with-pcre-jit \
    --with-sha1-asm \
    --with-stream \
    --with-stream_ssl_module \
    --with-threads \
    "

RUN apk add --no-cache --virtual .build-deps \
        build-base \
        curl \
        gd-dev \
        geoip-dev \
        libxslt-dev \
        linux-headers \
        make \
        perl-dev \
        readline-dev \
        zlib-dev

RUN apk add --no-cache \
        gd \
        geoip \
        libgcc \
        libxslt \
        zlib

COPY vendor/* /tmp/

RUN cd /tmp \
    && curl -fSL https://www.openssl.org/source/openssl-${RESTY_OPENSSL_VERSION}.tar.gz -o openssl-${RESTY_OPENSSL_VERSION}.tar.gz \
    && tar xzf openssl-${RESTY_OPENSSL_VERSION}.tar.gz \

    && curl -fSL https://ftp.pcre.org/pub/pcre/pcre-${RESTY_PCRE_VERSION}.tar.gz -o pcre-${RESTY_PCRE_VERSION}.tar.gz \
    && tar xzf pcre-${RESTY_PCRE_VERSION}.tar.gz \

    && curl -fSL https://openresty.org/download/openresty-${RESTY_VERSION}.tar.gz -o openresty-${RESTY_VERSION}.tar.gz \
    && tar xzf openresty-${RESTY_VERSION}.tar.gz \
    && cd /tmp/openresty-${RESTY_VERSION} \
    && ./configure -j1 ${RESTY_CONFIG_OPTIONS} \
    && make -j1 \
    && make -j1 install \
    && rm -rf /tmp/* \
    && apk del .build-deps


ENV PATH=$PATH:/usr/local/openresty/luajit/bin:/usr/local/openresty/nginx/sbin:/usr/local/openresty/bin

ENV openresty /usr/local/openresty

COPY ssl/nginx-auth.key /etc/ssl/private/nginx-auth.key
COPY ssl/nginx-auth.crt /etc/ssl/certs/nginx-auth.crt
COPY ssl/nginx-auth.pem /etc/ssl/certs/nginx-auth.pem

COPY src/nginx/nginx.nginx ${openresty}/nginx/conf/nginx.conf
COPY src/nginx/ssl.nginx ${openresty}/nginx/conf/ssl.nginx
COPY src/nginx/proxy_params.nginx ${openresty}/nginx/conf/proxy_params

COPY src/nginx/conf.d /etc/nginx/conf.d/

COPY src/vendor/ ${openresty}/lualib/
COPY src/lua ${openresty}/lualib/

EXPOSE 443
CMD ["/usr/local/openresty/bin/openresty", "-g", "daemon off;"]
STOPSIGNAL SIGQUIT