FROM alpine:3.10
LABEL mantainer 'Thiago Rocha <me@thiroc.me'

RUN apk update && apk upgrade
RUN apk add --no-cache git
RUN apk add --no-cache git-daemon
RUN apk add --no-cache curl

RUN addgroup -S git && adduser -S git -G git
USER git
WORKDIR /home/git

RUN mkdir repo content
RUN cd repo && \
	git init --bare

COPY --chown=git:git ./post-receive ./repo/hooks/
RUN chmod +x ./repo/hooks/post-receive

ENTRYPOINT ["git", "daemon", "--enable=receive-pack", "--base-path=.", "--export-all", "."]
