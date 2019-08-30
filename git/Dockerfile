FROM alpine:3.10
LABEL mantainer 'Thiago Rocha <me@thiroc.me'

RUN apk update && apk upgrade

RUN useradd git
USER git
WORKDIR /home/git

RUN apk add --update git

RUN mkdir repo content
RUN cd repo && \
	git init --bare

COPY post-receive ~/repo/hooks/
RUN chmod +x ~/repo/hooks/post-receive
