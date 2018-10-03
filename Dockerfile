FROM python:alpine3.7

COPY . /opt

ENV SSH_PASSWD "root:Docker!"
RUN apk update \
        && apk add openssh-server \
        vim \
        git \
        gcc \
        g++ \
        build-essential \
        curl \
        gnupg \
    && echo "$SSH_PASSWD" | chpasswd \
    && chmod 755 /opt/init_container.sh

COPY sshd_config /etc/ssh/

RUN pip install flask flask_restful 

EXPOSE 2222 8080

ENV PORT 8080

ENTRYPOINT ["/opt/init_container.sh"]
