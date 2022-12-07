#!/bin/sh

if [ $# -eq 0 ]
#if there are arguments
then
    echo "No arguments supplied..."

    read -p "Enter tag name [web/server]: " TAG_NAME
    TAG_NAME=${TAG_NAME:-web/server}

    read -p "Enter tag version [0.1.0]: " TAG_VERSION
    TAG_VERSION=${TAG_VERSION:-0.1.0}

    read -p "Enter dist directory name [dist]: " DIRECTORY_DIST_NAME
    DIRECTORY_DIST_NAME=${DIRECTORY_DIST_NAME:-dist}

    read -p "Enter dist directory path (absolute path please) [${PWD}]: " DIRECTORY_DIST_PATH
    DIRECTORY_DIST_PATH=${DIRECTORY_DIST_PATH:-${PWD}}

#else parse arguments
elif [ $# -eq 4 ]
then
    #flags parsing
    while getopts n:v:d:p: flag
    do
        case "${flag}" in
            n) TAG_NAME=${OPTARG};;
            v) TAG_VERSION=${OPTARG};;
            d) DIRECTORY_DIST_NAME=${OPTARG};;
            p) DIRECTORY_DIST_PATH=${OPTARG};;
        esac
    done
fi

#directory dist copying
if [ ${DIRECTORY_DIST_PATH}/${DIRECTORY_DIST_NAME} != ${PWD}/${DIRECTORY_DIST_NAME} ]
then
    { # try
        mkdir ${PWD}/${DIRECTORY_DIST_NAME};
    } || { # catch
        rm -rfdv ${PWD}/${DIRECTORY_DIST_NAME};
        cp --copy-contents --recursive ${DIRECTORY_DIST_PATH}/${DIRECTORY_DIST_NAME} ${PWD}/${DIRECTORY_DIST_NAME} ;
    }
fi

echo "Building image: $TAG_NAME:$TAG_VERSION..."
docker build . -t $TAG_NAME:$TAG_VERSION
