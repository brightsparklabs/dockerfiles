#!/usr/bin/env sh

##
 # Entrypoint script
 # _____________________________________________________________________________
 #
 # Created by brightSPARK Labs
 # www.brightsparklabs.com
 ##

if [ "$1" == "--daemon" ]
then
    exec crond -f -d 8
else
    exec /app/ns1_ddns.py
fi

