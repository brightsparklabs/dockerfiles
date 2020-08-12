##
 # Alpine based image for running bslcli.
 # _____________________________________________________________________________
 #
 # Created by brightSPARK Labs
 # www.brightsparklabs.com
 ##

FROM python
MAINTAINER brightSPARK Labs <enquire@brightsparklabs.com>
LABEL Description="Alpine based image for running bslcli" Vendor="brightSPARK Labs"

COPY app /app
WORKDIR /app
ENTRYPOINT ["./entrypoint.sh"]

