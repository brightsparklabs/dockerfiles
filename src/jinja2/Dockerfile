##
 # Alpine based Jinja2 image.
 # _____________________________________________________________________________
 #
 # Created by brightSPARK Labs
 # www.brightsparklabs.com
 ##

FROM python:2.7.12-alpine
MAINTAINER brightSPARK Labs <enquire@brightsparklabs.com>
LABEL Description="Alpine based Jinja2 image." Vendor="brightSPARK Labs"

RUN \
    apk add --no-cache \
        bash=4.3.42-r5 \
        py-pip=8.1.2-r0 && \
    pip install --force-reinstall \
        PyYAML==3.11 \
        j2cli==0.3.1-0 && \
    apk del py-pip

