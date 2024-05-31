#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

Copyright (c) 2024 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""

__author__ = "Gabriel Zapodeanu TME, ENB"
__email__ = "gzapodea@cisco.com"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2024 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"

import requests
import urllib3
import json
import os
import time
import pprint

from dotenv import load_dotenv

from urllib3.exceptions import InsecureRequestWarning  # for insecure https warnings
from requests.auth import HTTPBasicAuth  # for Basic Auth

os.environ['TZ'] = 'America/Los_Angeles'  # define the timezone for PST
time.tzset()  # adjust the timezone, more info https://help.pythonanywhere.com/pages/SettingTheTimezone/

urllib3.disable_warnings(InsecureRequestWarning)  # disable insecure https warnings

load_dotenv('environment.env')

WEBHOOK_URL = os.getenv('WEBHOOK_URL')
WEBHOOK_USERNAME = os.getenv('WEBHOOK_USERNAME')
WEBHOOK_PASSWORD = os.getenv('WEBHOOK_PASSWORD')

BASIC_AUTH = HTTPBasicAuth(WEBHOOK_USERNAME, WEBHOOK_PASSWORD)

webhook_payload_active = {
    "version": "1.0.0",
    "efInstanceId": "5e3860db-6043-481d-b79c-5edad0f1a389",
    "instanceId": "7fd7fb19-f382-4a8b-95c4-78959d43c9a7",
    "eventId": "NETWORK-NETWORKS-2-272",
    "namespace": "ASSURANCE",
    "name": "",
    "description": "",
    "type": "NETWORK",
    "category": "ERROR",
    "domain": "Know Your Network",
    "subDomain": "Networks",
    "severity": 1,
    "source": "ndp",
    "timestamp": 1715185019597,
    "details": {
        "Type": "Network Device",
        "Assurance Issue Details": "Device:PDX-RO - BGP is down with neighbor 10.93.141.42",
        "Assurance Issue Priority": "P1",
        "Device": "10.93.141.23",
        "Assurance Issue Name": "BGP is Down on Device PDX-RO with Neighbor 10.93.141.42",
        "Assurance Issue Category": "connectivity",
        "Assurance Issue Status": "active"
    },
    "ciscoDnaEventLink": "https://10.93.141.45/dna/assurance/issueDetails?issueId=7fd7fb19-f382-4a8b-95c4-78959d43c9a7",
    "note": "To programmatically get more info see here - https://<ip-address>/dna/platform/app/consumer-portal/developer-toolkit/apis?apiId=8684-39bb-4e89-a6e4",
    "context": "",
    "userId": "",
    "i18n": "",
    "eventHierarchy": "",
    "message": "",
    "messageParams": "",
    "parentInstanceId": "",
    "network": {
        "siteId": "/15ab86e1-706e-41df-8400-ee1a974bc1f3/245892a8-21e9-4d30-9e36-67c44a120d3b/15628823-b52e-4564-a39c-36a9d45dc180/17d5b2b9-ff29-4320-bdab-fd6c3d7df09d/",
        "deviceId": "01f7cdf2-2298-42c7-bb74-dc68e3c3a051"
    },
    "dnacIP": "10.93.141.45",
    "correlationId": "54bccda5-b79a-4f3a-9787-b0e33a7da1dd"
}

webhook_payload_resolved = {
    "version": "1.0.0",
    "efInstanceId": "5e3860db-6043-481d-b79c-5edad0f1a389",
    "instanceId": "7fd7fb19-f382-4a8b-95c4-78959d43c9a7",
    "eventId": "NETWORK-NETWORKS-2-272",
    "namespace": "ASSURANCE",
    "name": "",
    "description": "",
    "type": "NETWORK",
    "category": "ERROR",
    "domain": "Know Your Network",
    "subDomain": "Networks",
    "severity": 1,
    "source": "ndp",
    "timestamp": 1715185019597,
    "details": {
        "Type": "Network Device",
        "Assurance Issue Details": "Device:PDX-RO - BGP is down with neighbor 10.93.141.42",
        "Assurance Issue Priority": "P1",
        "Device": "10.93.141.23",
        "Assurance Issue Name": "BGP is Down on Device PDX-RO with Neighbor 10.93.141.42",
        "Assurance Issue Category": "connectivity",
        "Assurance Issue Status": "resolved"
    },
    "ciscoDnaEventLink": "https://10.93.141.45/dna/assurance/issueDetails?issueId=7fd7fb19-f382-4a8b-95c4-78959d43c9a7",
    "note": "To programmatically get more info see here - https://<ip-address>/dna/platform/app/consumer-portal/developer-toolkit/apis?apiId=8684-39bb-4e89-a6e4",
    "context": "",
    "userId": "",
    "i18n": "",
    "eventHierarchy": "",
    "message": "",
    "messageParams": "",
    "parentInstanceId": "",
    "network": {
        "siteId": "/15ab86e1-706e-41df-8400-ee1a974bc1f3/245892a8-21e9-4d30-9e36-67c44a120d3b/15628823-b52e-4564-a39c-36a9d45dc180/17d5b2b9-ff29-4320-bdab-fd6c3d7df09d/",
        "deviceId": "01f7cdf2-2298-42c7-bb74-dc68e3c3a051"
    },
    "dnacIP": "10.93.141.45",
    "correlationId": "54bccda5-b79a-4f3a-9787-b0e33a7da1dd"
}

# test the Webhook with a Cisco Catalyst Center notification

url = WEBHOOK_URL
header = {'content-type': 'application/json'}
response = requests.post(url, auth=BASIC_AUTH, data=json.dumps(webhook_payload_active), headers=header, verify=False)
print(response.status_code, response.text)





