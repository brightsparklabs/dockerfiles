#!/usr/bin/env python3
# # -*- coding: utf-8 -*-

"""
Dynamic DNS Update for NS1
________________________________________________________________________________

Created by brightSPARK Labs
www.brightsparklabs.com
"""

import logging
import socket

from ns1 import NS1
import click
import requests
import yaml

# ------------------------------------------------------------------------------
# LOGGING
# ------------------------------------------------------------------------------

FORMAT = '%(asctime)s %(levelname)s: %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
logger = logging.getLogger(__name__)

# ------------------------------------------------------------------------------
# CLI FUNCTIONS
# ------------------------------------------------------------------------------

@click.command()
@click.option('--api-key', required=True, help='NS1 api key')
@click.option('--hostname', required=False, help='hostname for the record')
@click.option('--domain', required=True, help='domain name for the record')
def main(api_key, domain, hostname=None):
    client = NS1(apiKey=api_key)
    client.config["transport"] = "requests"
    if hostname == None:
        hostname = socket.gethostname()
    zone = client.loadZone(domain)
    current_ip = requests.get("https://api.ipify.org/?format=json").json()["ip"]

    try:
        record = zone.loadRecord(hostname, 'A')
        dns_ip = record.data['answers'][0]['answer'][0]
        if current_ip != dns_ip:
            logger.info('Updating [%s.%s -> %s] ...', hostname, domain, current_ip)
            record.update(answers=[current_ip])
        else:
            logger.info('DNS record exists [%s.%s -> %s] ...', hostname, domain, current_ip)

    except:
        logger.info('Creating [%s.%s -> %s] ...', hostname, domain, current_ip)
        zone.add_A(hostname, answers=[current_ip])

if __name__ == "__main__":
    main(auto_envvar_prefix='NS1')

