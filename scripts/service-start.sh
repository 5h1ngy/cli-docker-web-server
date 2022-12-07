#!/bin/sh

read -p "Enter container name [web-server]: " CONTAINER_NAME
CONTAINER_NAME=${CONTAINER_NAME:-web-server}

read -p "Enter container port [8085]: " CONTAINER_PORT
CONTAINER_PORT=${CONTAINER_PORT:-8085}

read -p "Enter container SSL port [8086]: " CONTAINER_SSL_PORT
CONTAINER_SSL_PORT=${CONTAINER_SSL_PORT:-8086}

echo 'container Starting...'; 
docker run --detach \
    --publish ${CONTAINER_PORT}:80 --publish ${CONTAINER_SSL_PORT}:81 \
    --name ${CONTAINER_NAME} web/server:0.1.0;