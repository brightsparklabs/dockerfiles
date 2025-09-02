##
 # Python3 based image with ansible and plugins to support AWS modules and SSM.
 # _____________________________________________________________________________
 #
 # Created by brightSPARK Labs
 # www.brightsparklabs.com
 ##

FROM python:3.13.7-slim

# Set the `PATH` for `pipx` installs.
ENV PATH="/root/.local/bin:${PATH}"

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get -y install curl pipx \
    && apt-get clean \
    && rm -fr /var/lib/apt/lists/* \
    && pipx install --include-deps ansible \
    && ansible-galaxy collection install community.aws community.general \
    && ansible-galaxy install christiangda.amazon_cloudwatch_agent \
    && curl "https://s3.amazonaws.com/session-manager-downloads/plugin/latest/ubuntu_64bit/session-manager-plugin.deb" \
      -o "session-manager-plugin.deb" \
    && apt install ./session-manager-plugin.deb
COPY --from=docker:dind /usr/local/bin/docker /usr/local/bin/

ENTRYPOINT ["/bin/bash"]

ARG APP_VERSION
ARG BUILD_DATE
ARG VCS_REF
LABEL org.label-schema.name="ansible-aws" \
      org.label-schema.description="Python3 based image with ansible and plugins to support AWS modules and SSM." \
      org.label-schema.vendor="brightSPARK Labs" \
      org.label-schema.schema-version="1.0.0-rc1" \
      org.label-schema.vcs-url="https://github.com/brightsparklabs/dockerfiles" \
      org.label-schema.vcs-ref=${VCS_REF} \
      org.label-schema.build-date=${BUILD_DATE} \
      org.label-schema.version=${APP_VERSION}
ENV META_BUILD_DATE=${BUILD_DATE}
ENV META_VCS_REF=${VCS_REF}
ENV APP_VERSION=${APP_VERSION}
