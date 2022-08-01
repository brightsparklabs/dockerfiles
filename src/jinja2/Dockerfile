##
 # Alpine based Jinja2 image.
 # _____________________________________________________________________________
 #
 # Created by brightSPARK Labs
 # www.brightsparklabs.com
 ##

FROM python:3.10.5-alpine3.16
LABEL Maintainer="brightSPARK Labs <enquire@brightsparklabs.com>"
LABEL Description="Alpine based Jinja2 image." Vendor="brightSPARK Labs"

RUN \
    apk add --no-cache \
        bash=5.1.16-r2 \
        make=4.3-r0 && \
    pip install --force-reinstall \
        PyYAML==6.0 \
        jinja2-cli==0.8.2
