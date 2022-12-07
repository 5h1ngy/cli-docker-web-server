#!/bin/sh

{ # try
    mkdir ${PWD}/dumps;
} || { # catch
    echo "${PWD}/dumps: directory already exists"
    echo "removing..."
    rm -rfdv ${PWD}/dumps/;
}

docker image save --output ${PWD}/dumps/nginx_1.23.2_alpine.tar nginx:1.23.2-alpine