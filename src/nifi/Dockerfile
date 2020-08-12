##
 # Alpine based Apache NiFi image.
 # _____________________________________________________________________________
 #
 # Created by brightSPARK Labs
 # www.brightsparklabs.com
 ##

FROM brightsparklabs/java8:g1.0.0
LABEL Maintainer="brightSPARK Labs <enquire@brightsparklabs.com>"
LABEL Description="Alpine based Apache NiFi image." Vendor="brightSPARK Labs"

ENV NIFI_VERSION 1.2.0
ENV NIFI_HOME /opt/nifi

# Download and Install nifi
RUN wget -q http://archive.apache.org/dist/nifi/$NIFI_VERSION/nifi-$NIFI_VERSION-bin.tar.gz && \
   tar xzf nifi-$NIFI_VERSION-bin.tar.gz -C /opt/ && \
   ln -s /opt/nifi-$NIFI_VERSION $NIFI_HOME && \
   rm nifi-$NIFI_VERSION-bin.tar.gz && \
   sed -i -e "s|^nifi.ui.banner.text=.*$$|nifi.ui.banner.text=My Docker NiFi - $NIFI_VERSION|" $NIFI_HOME/conf/nifi.properties && \
   sed -i 's/\.\/conf\/flow\.xml\.gz/\.\/flow_configuration\/flow.xml.gz/' ${NIFI_HOME}/conf/nifi.properties && \
   mkdir $NIFI_HOME/database_repository && \
   mkdir $NIFI_HOME/flowfile_repository && \
   mkdir $NIFI_HOME/content_repository && \
   mkdir $NIFI_HOME/provenance_repository && \
   mkdir $NIFI_HOME/flow_configuration

VOLUME ["$NIFI_HOME/conf", "$NIFI_HOME/database_repository", "$NIFI_HOME/flowfile_repository", "$NIFI_HOME/content_repository", "$NIFI_HOME/provenance_repository", "${NIFI_HOME}/flow_configuration", "${NIFI_HOME}/state/local"]

# Nifi Web port
EXPOSE 8080
EXPOSE 9443

WORKDIR $NIFI_HOME

CMD ["bin/nifi.sh", "run"]
