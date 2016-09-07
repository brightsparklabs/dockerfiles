##
 # Alpine based Oracle Java 8 JRE image with Groovy 2.4.5.
 # _____________________________________________________________________________
 #
 # Created by brightSPARK Labs
 # www.brightsparklabs.com
 ##

FROM brightsparklabs/java8:g1.0.0 
MAINTAINER brightSPARK Labs <enquire@brightsparklabs.com>
LABEL Description="Alpine based Oracle Java 8 JRE image with Groovy 2.4.5" Vendor="brightSPARK Labs"

ENV GROOVY_VERSION=2.4.5
ENV GROOVY_HOME=/opt/groovy
ENV PATH ${PATH}:${GROOVY_HOME}/bin

# Install groovy
ADD http://dl.bintray.com/groovy/maven/apache-groovy-binary-${GROOVY_VERSION}.zip /tmp/

RUN \
  unzip -d /opt/ /tmp/apache-groovy-binary-${GROOVY_VERSION}.zip && \
  rm /tmp/apache-groovy-binary-${GROOVY_VERSION}.zip && \
  ln -s /opt/groovy-${GROOVY_VERSION} /opt/groovy

# Workaround to run groovy in alpine - https://issues.apache.org/jira/browse/GROOVY-7906
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
