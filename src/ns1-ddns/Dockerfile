##
 # Alpine based image for performing dynamic DNS updates with NS1.
 # _____________________________________________________________________________
 #
 # Created by brightSPARK Labs
 # www.brightsparklabs.com
 ##

FROM python:alpine
MAINTAINER brightSPARK Labs <enquire@brightsparklabs.com>
LABEL Description="Alpine based image for performing dynamic DNS updates with NS1." Vendor="brightSPARK Labs"

COPY crontab /etc/crontabs/root
COPY app/ /app
WORKDIR /app
RUN apk add --no-cache git \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del --no-cache git
ENTRYPOINT ["/app/entrypoint.sh"]

