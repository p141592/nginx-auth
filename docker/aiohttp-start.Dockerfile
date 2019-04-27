FROM python:3.6
RUN pip install aiohttp
COPY ./src/ /opt/application
WORKDIR /opt/application
