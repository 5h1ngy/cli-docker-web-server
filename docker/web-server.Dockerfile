FROM nginx:1.23.2-alpine
ARG STATIC_DIR

COPY ${PWD}/nginx/health-check.conf /etc/nginx/conf.d/health-check.conf
COPY ${PWD}/nginx/nginx.conf /etc/nginx/nginx.conf
COPY ${PWD}/nginx/index.conf /etc/nginx/conf.d/
COPY ${PWD}/public/${STATIC_DIR}/ /usr/share/nginx/html/

EXPOSE 80/tcp

CMD ["/usr/sbin/nginx", "-g", "daemon off;"]