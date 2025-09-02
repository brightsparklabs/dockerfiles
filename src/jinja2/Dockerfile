##
 # Alpine based Jinja2 image.
 # _____________________________________________________________________________
 #
 # Created by brightSPARK Labs
 # www.brightsparklabs.com
 ##

FROM python:3.12.11-alpine3.22

RUN \
    apk add --no-cache \
        bash~=5.2.37-r0 \
        git~=2.49.1-r0 \
        make~=4.4.1-r3 && \
    pip install --force-reinstall \
        PyYAML~=6.0.2 \
        jinja2-cli~=0.8.2

ARG APP_VERSION
ARG BUILD_DATE
ARG VCS_REF
LABEL org.label-schema.name="jinja2" \
      org.label-schema.description="Alpine based Jinja2 image." \
      org.label-schema.vendor="brightSPARK Labs" \
      org.label-schema.schema-version="1.0.0-rc1" \
      org.label-schema.vcs-url="https://github.com/brightsparklabs/dockerfiles" \
      org.label-schema.vcs-ref=${VCS_REF} \
      org.label-schema.build-date=${BUILD_DATE} \
      org.label-schema.version=${APP_VERSION}
ENV META_BUILD_DATE=${BUILD_DATE}
ENV META_VCS_REF=${VCS_REF}
ENV APP_VERSION=${APP_VERSION}
