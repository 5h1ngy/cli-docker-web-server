#!/bin/sh

{ # try
    docker image load --input ${PWD}/dumps/nginx_1.23.2_alpine.tar
} || { # catch
    echo "${PWD}/dumps/nginx_1.23.2_alpine.tar: archive not found"
}