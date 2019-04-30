FROM nginx:1.15

# network test tools
RUN apt update -y && apt install -y iputils-ping net-tools curl wget nmap

# log,logrotate setting
COPY config/nginx /etc/logrotate.d/nginx
