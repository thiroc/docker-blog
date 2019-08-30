FROM python:3.6
LABEL maintainer 'Thiago Rocha <me@thiroc.me>'

# Initial setup
RUN apt update && apt upgrade -y && \
	apt install python3 python3-pip -y && \
	pip install pelican markdown
RUN mkdir -p /srv/pelican/content && \
	cd /srv/pelican

# Copy relevant pelican files
COPY ./content/first.md /srv/pelican/content
COPY pelicanconf.py /srv/pelican/
COPY publishconf.py /srv/pelican/
COPY Makefile /srv/pelican/

WORKDIR /srv/pelican
