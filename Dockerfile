FROM wordpress:latest

ENV SSH_PASSWD "root:Docker!"
RUN apt-get update \
    && apt-get install -y --no-install-recommends openssh-server \
    && echo "root:Docker!" | chpasswd \
    && chmod 755 /opt/init_container.sh

COPY sshd_config /etc/ssh/


EXPOSE 2222 8080

ENV PORT 8080

ENTRYPOINT ["/opt/init_container.sh"]
