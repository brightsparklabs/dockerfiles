##
 # Python3 based image with ansible and plugins to support AWS modules and SSM.
 # _____________________________________________________________________________
 #
 # Created by brightSPARK Labs
 # www.brightsparklabs.com
 ##

FROM python:3.8.7-slim
LABEL Maintainer="brightSPARK Labs <enquire@brightsparklabs.com>" \
    Description="Python3 based image with ansible and plugins to support AWS modules and SSM." \
    Vendor="brightSPARK Labs"

RUN python -m pip install ansible boto3 docker && \
    ansible-galaxy collection install community.aws community.general && \
    ansible-galaxy install christiangda.amazon_cloudwatch_agent && \
    apt update && \
    apt install -y curl && \
    curl "https://s3.amazonaws.com/session-manager-downloads/plugin/latest/ubuntu_64bit/session-manager-plugin.deb" -o "session-manager-plugin.deb" && \
    apt install ./session-manager-plugin.deb

ENTRYPOINT ["/bin/bash"]
