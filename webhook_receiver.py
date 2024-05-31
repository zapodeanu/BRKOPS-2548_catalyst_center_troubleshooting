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

__author__ = "Gabriel Zapodeanu PTME"
__email__ = "gzapodea@cisco.com"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2024 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"

import json
import logging
import os
import time

import requests
import urllib3
from dotenv import load_dotenv
from flask import Flask, request
from flask_basicauth import BasicAuth
from urllib3.exceptions import InsecureRequestWarning  # for insecure https warnings

os.environ['TZ'] = 'America/Los_Angeles'  # define the timezone for PST
time.tzset()  # adjust the timezone, more info https://help.pythonanywhere.com/pages/SettingTheTimezone/

urllib3.disable_warnings(InsecureRequestWarning)  # disable insecure https warnings

load_dotenv('environment.env')

WEBHOOK_URL = os.getenv('WEBHOOK_URL')
WEBHOOK_USERNAME = os.getenv('WEBHOOK_USERNAME')
WEBHOOK_PASSWORD = os.getenv('WEBHOOK_PASSWORD')

JENKINS_API_TOKEN = os.getenv('JENKINS_API_TOKEN')
JENKINS_USER = os.getenv('JENKINS_USER')
JENKINS_URL = os.getenv('JENKINS_URL')

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = WEBHOOK_USERNAME
app.config['BASIC_AUTH_PASSWORD'] = WEBHOOK_PASSWORD
app.config['BASIC_AUTH_FORCE'] = True

basic_auth = BasicAuth(app)

# logging, debug level, to file {application_run.log}
logging.basicConfig(level=logging.INFO)


@app.route('/')  # create a page for testing the flask framework
@basic_auth.required
def index():
    return '<h1>Flask Receiver App is Up!</h1>', 200


# noinspection PyGlobalUndefined
@app.route('/troubleshooting', methods=['POST'])  # create a route for /troubleshooting, method POST, receive events
@basic_auth.required
def webhook():
    global status_message
    if request.method == 'POST':
        logging.info(' Webhook Received')
        request_json = request.json

        # log.info the received notification
        logging.info('Payload: ')
        logging.info(request_json)

        # save as a file, create new file if not existing, append to existing file
        # full details of each notification to file 'all_webhooks_detailed.json'

        with open('webhooks_detailed.json', 'a') as filehandle:
            filehandle.write('%s\n' % json.dumps(request_json))

        # parse the issue Id from the received notification
        notification = request_json
        issue_id = notification['instanceId']

        # check if issue active or resolved
        if notification['details']['Assurance Issue Status'] == 'active':
            logging.info(' New issue, will trigger Jenkins pipeline - Network Troubleshooting')
            url = JENKINS_URL + 'job/Network%20Troubleshooting/buildWithParameters?assuranceIssueId=' + issue_id
            response = requests.post(url, auth=(JENKINS_USER, JENKINS_API_TOKEN), verify=False)

            if response.status_code == 201:
                status_message = 'Pipeline triggered'
            else:
                status_message = 'Pipeline not triggered. Response: ' + response.text
            logging.info(' Issue Id: ' + issue_id + ' status: ' + status_message)
        else:
            logging.info(' Issue resolved or ignored')

        return status_message, 202
    else:
        return 'POST Method not supported', 405


if __name__ == '__main__':
    app.run(port=5443, ssl_context='adhoc', debug=True)



