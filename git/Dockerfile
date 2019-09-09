FROM alpine:3.10
LABEL mantainer 'Thiago Rocha <me@thiroc.me'

RUN apk update && apk upgrade
RUN apk add --no-cache git
RUN apk add --no-cache openssh
RUN apk add --no-cache curl

RUN ssh-keygen -A

RUN addgroup git && \
	adduser -D -s /usr/bin/git-shell git -G git && \
	echo git:123456 | chpasswd
#USER git

RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config && \
	sed -i 's/#PubkeyAuthentication/PubkeyAuthentication/' /etc/ssh/sshd_config && \
	echo "RSAAuthentication yes" >> /etc/ssh/sshd_config

WORKDIR /home/git

RUN mkdir repo content keys .ssh
RUN git init --bare --shared=true ./repo

COPY ./post-receive ./repo/hooks/
COPY ./start.sh ./start.sh

VOLUME ./keys
EXPOSE 22
ENTRYPOINT ["sh", "start.sh"]
