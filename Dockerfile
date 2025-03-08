#FROM python:3.8-alpine
#
#RUN mkdir -p /usr/src/app
#WORKDIR /usr/src/app
#
#COPY requirements.txt /usr/src/app/
#
#RUN pip3 install --no-cache-dir -r requirements.txt
#
#COPY . /usr/src/app
#
#EXPOSE 8080
#
#ENTRYPOINT ["python3"]
#
#CMD ["-m", "swagger_server"]

FROM python:3.8-alpine

# Install bash, coreutils, and other basic utilities
RUN apk add --no-cache bash coreutils

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 8080

ENTRYPOINT ["python3"]
CMD ["-m", "swagger_server"]
