##
 # This image is effectively a fork of `razorcreationsltd/puppeteer-pipelines` that uses a newer version of `node` as the base image.
 # See the `Dockerfile` here: `https://github.com/razorcreations/puppeteer-pipelines`.

 # We use this image as part of our Bitbucket Pipelines to build node applications that depend on `puppeteer`.
 # _____________________________________________________________________________
 #
 # Created by brightSPARK Labs
 # www.brightsparklabs.com
 ##

FROM node:24.7.0-trixie

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    fonts-ipafont-gothic \
    fonts-kacst-one \
    fonts-thai-tlwg \
    fonts-freefont-ttf \
    apt-transport-https \
    ca-certificates \
    curl \
  && curl -fSsL https://dl.google.com/linux/linux_signing_key.pub \
    | gpg --dearmor \
    | tee /usr/share/keyrings/google-chrome.gpg > /dev/null \
  && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome.gpg] http://dl.google.com/linux/chrome/deb/ stable main" \
    | tee /etc/apt/sources.list.d/google-chrome.list \
  && apt-get update \
  && apt-get install -y --no-install-recommends google-chrome-stable \
  && rm -rf /var/lib/apt/lists/* \
  && apt-get purge --auto-remove -y curl

ARG APP_VERSION
ARG BUILD_DATE
ARG VCS_REF
LABEL org.label-schema.name="puppeteer-pipelines" \
      org.label-schema.description="Newer version of node for puppeteer use in the Bitbucket Pipelines." \
      org.label-schema.vendor="brightSPARK Labs" \
      org.label-schema.schema-version="1.0.0-rc1" \
      org.label-schema.vcs-url="https://github.com/brightsparklabs/dockerfiles" \
      org.label-schema.vcs-ref=${VCS_REF} \
      org.label-schema.build-date=${BUILD_DATE} \
      org.label-schema.version=${APP_VERSION}
ENV META_BUILD_DATE=${BUILD_DATE}
ENV META_VCS_REF=${VCS_REF}
ENV APP_VERSION=${APP_VERSION}
