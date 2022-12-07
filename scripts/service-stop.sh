#!/bin/sh
#!/bin/sh

read -p "Enter container name [web-server]: " CONTAINER_NAME
CONTAINER_NAME=${CONTAINER_NAME:-web-server}

docker container stop ${CONTAINER_NAME}; 
echo 'container stop: DONE!'; 
docker container rm ${CONTAINER_NAME}; 
echo 'container rm: DONE!'; 