##
 # Alpine based logstash image+glibc
 # _____________________________________________________________________________
 #
 # Created by brightSPARK Labs
 # www.brightsparklabs.com
 ##

FROM brightsparklabs/java8:g1.0.0
LABEL Maintainer="brightSPARK Labs <enquire@brightsparklabs.com>"
LABEL Description="Alpine based Logstash + glibc image." Vendor="brightSPARK Labs"

ENV LOGSTASH_VERSION 2.3.2

RUN \
    mkdir -p /opt/ && \
    # install logstash
    wget -O - http://download.elastic.co/logstash/logstash/logstash-${LOGSTASH_VERSION}.tar.gz | tar zxf - -C /opt && \
    ln -s /opt/logstash-${LOGSTASH_VERSION} /opt/logstash && \

    /opt/logstash/bin/logstash-plugin install logstash-filter-translate && \
    /opt/logstash/bin/logstash-plugin install logstash-output-syslog

CMD /opt/logstash/bin/logstash -f /etc/logstash/logstash.conf

