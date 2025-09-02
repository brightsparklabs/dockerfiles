##
 # Ubuntu based image with AWS CLI and some standard tools for CI-CD
 # _____________________________________________________________________________
 #
 # Created by brightSPARK Labs
 # www.brightsparklabs.com
 ##

FROM ubuntu:24.04

# Set the `PATH` for `pipx` installs.
ENV PATH="/root/.local/bin:${PATH}"

# Install utility packages
RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get -y install python3 pipx bash jq openssh-client git curl \
  && apt-get clean \
  && rm -fr /var/lib/apt/lists/* \
  && pipx install awscli \
  && curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash

ENTRYPOINT ["/bin/bash"]

ARG APP_VERSION
ARG BUILD_DATE
ARG VCS_REF
LABEL org.label-schema.name="aws-ci-cd" \
      org.label-schema.description="Ubuntu based image with AWS CLI and some standard tools for CI-CD" \
      org.label-schema.vendor="brightSPARK Labs" \
      org.label-schema.schema-version="1.0.0-rc1" \
      org.label-schema.vcs-url="https://github.com/brightsparklabs/dockerfiles" \
      org.label-schema.vcs-ref=${VCS_REF} \
      org.label-schema.build-date=${BUILD_DATE} \
      org.label-schema.version=${APP_VERSION}
ENV META_BUILD_DATE=${BUILD_DATE}
ENV META_VCS_REF=${VCS_REF}
ENV APP_VERSION=${APP_VERSION}
