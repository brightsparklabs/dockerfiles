##
 # Alpine based Oracle Java 8 JRE image.
 # _____________________________________________________________________________
 #
 # Created by brightSPARK Labs
 # www.brightsparklabs.com
 ##

FROM anapsix/alpine-java:8u102b14_server-jre_unlimited

ARG APP_VERSION
ARG BUILD_DATE
ARG VCS_REF
LABEL org.label-schema.name="java8" \
      org.label-schema.description="Alpine based Oracle Java 8 JRE image." \
      org.label-schema.vendor="brightSPARK Labs" \
      org.label-schema.schema-version="1.0.0-rc1" \
      org.label-schema.vcs-url="https://github.com/brightsparklabs/dockerfiles" \
      org.label-schema.vcs-ref=${VCS_REF} \
      org.label-schema.build-date=${BUILD_DATE} \
      org.label-schema.version=${APP_VERSION}
ENV META_BUILD_DATE=${BUILD_DATE}
ENV META_VCS_REF=${VCS_REF}
ENV APP_VERSION=${APP_VERSION}
