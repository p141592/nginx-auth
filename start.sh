#!/usr/bin/env bash

docker build -t nginx-lua . && docker run -d -p 8000:80 --name nginx-lua nginx-lua