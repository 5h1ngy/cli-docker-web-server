#!/bin/sh

mkdir ${PWD}/dumps; docker image save --output ${PWD}/dumps/web_server_0.1.0.tar web/server:0.1.0