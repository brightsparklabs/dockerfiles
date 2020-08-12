##
 # Node-Alpine based image with AWS CLI and some standard tools for CI-CD
 # _____________________________________________________________________________
 #
 # Created by brightSPARK Labs
 # www.brightsparklabs.com
 ##

FROM node:14.7.0-alpine
MAINTAINER brightSPARK Labs <enquire@brightsparklabs.com>
LABEL Description="Node-Alpine based image with AWS CLI and some standard tools for CI-CD" Vendor="brightSPARK Labs"

# install utility packages
RUN apk add --no-cache python
RUN apk add --no-cache py-pip
RUN apk add --no-cache bash
RUN apk add --no-cache jq
RUN apk add --no-cache openssh
RUN apk add --no-cache git
RUN pip install awscli

ENTRYPOINT ["/bin/bash"]
