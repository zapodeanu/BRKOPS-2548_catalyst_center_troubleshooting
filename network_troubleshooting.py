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

import argparse
import json
import logging
import os
import time
from datetime import datetime

import dnacentersdk
import urllib3
import yaml
from dotenv import load_dotenv
from urllib3.exceptions import InsecureRequestWarning  # for insecure https warnings

load_dotenv('environment.env')

CATALYST_CENTER_URL = os.getenv('CATALYST_CENTER_URL')
CATALYST_CENTER_USER = os.getenv('CATALYST_CENTER_USER')
CATALYST_CENTER_PASS = os.getenv('CATALYST_CENTER_PASS')

os.environ['TZ'] = 'America/Los_Angeles'  # define the timezone for PST
time.tzset()  # adjust the timezone, more info https://help.pythonanywhere.com/pages/SettingTheTimezone/

urllib3.disable_warnings(InsecureRequestWarning)  # disable insecure https warnings

load_dotenv('environment.env')

# logging, debug level, to file {application_run.log}
logging.basicConfig(level=logging.INFO)


def main():
    """
    This application will automate network troubleshooting of network devices using Catalyst Center APIs.
    The application will run on Jenkins and requires one parameter to be received - Issue unique identifier
    - It will collect the issue details using the Issue Enrichment API
    - device details calling the Get Device Detail API
    - compliance of the device reporting the issue
    - call Execute Suggested Actions API
    - execute all commands from knowledge base calling Command Runner APIs
    :return:
    """

    # logging basic
    logging.basicConfig(level=logging.INFO)

    current_time = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    logging.info(' App "Network Troubleshooting.py" run start, ' + current_time)

    # parse the input arguments
    parser = argparse.ArgumentParser(description="A script that accepts one argument")
    parser.add_argument("assuranceIssueId", help="The Assurance issue Id")

    args = parser.parse_args()
    issue_id = args.assuranceIssueId

    logging.info(' The Assurance issue Id received is: ' + issue_id)

    # create a Catalyst Center connection object to use the Python SDK
    cc_api = dnacentersdk.DNACenterAPI(username=CATALYST_CENTER_USER, password=CATALYST_CENTER_PASS,
                                       base_url=CATALYST_CENTER_URL, version='2.3.5.3', verify=False)

    # retrieve the issue enrichment details
    headers = {'entity_type': 'issue_id', 'entity_value': issue_id}
    issue_details = cc_api.issues.get_issue_enrichment_details(headers=headers)
    device_id = issue_details['issueDetails']['issue'][0]['deviceId']
    issue_description = issue_details['issueDetails']['issue'][0]['issueDescription']
    issue_name = issue_details['issueDetails']['issue'][0]['issueName']
    issue_timestamp = issue_details['issueDetails']['issue'][0]['issueTimestamp']/1000
    issue_localtime = datetime.fromtimestamp(issue_timestamp).strftime('%c')
    issue_summary = issue_details['issueDetails']['issue'][0]['issueSummary']
    issue_priority = issue_details['issueDetails']['issue'][0]['issuePriority']
    issue_severity = issue_details['issueDetails']['issue'][0]['issueSeverity']

    # log issue details
    logging.info('\n--------------------------------------------------------------------\n')
    logging.info(' The issue details')
    logging.info('   Severity: ' + issue_severity)
    logging.info('   Priority: ' + issue_priority)
    logging.info('   Issue name: ' + issue_name)
    logging.info('   Summary: ' + issue_summary)
    logging.info('   Description: ' + issue_description)
    logging.info('   Timestamp: ' + issue_localtime)
    issue_details_link = CATALYST_CENTER_URL + '/dna/assurance/issueDetails?issueId=' + issue_id
    logging.info('   Issue Details: ' + issue_details_link)

    # retrieve the device details
    device_details = cc_api.devices.get_device_detail(identifier='uuid', search_by=device_id)
    device_hostname = device_details['response']['nwDeviceName']
    device_management_ip_address = device_details['response']['managementIpAddr']
    device_serial_number = device_details['response']['serialNumber']
    device_health = device_details['response']['overallHealth']
    device_role = device_details['response']['nwDeviceRole']
    device_family = device_details['response']['platformId']
    device_software = device_details['response']['softwareVersion']
    device_reachable = device_details['response']['communicationState']
    device_location = device_details['response']['location']

    # log device details
    logging.info('\n--------------------------------------------------------------------\n')
    logging.info(' The device details')
    logging.info('   Hostname: ' + device_hostname)
    logging.info('   Location: ' + device_location)
    logging.info('   Device Role: ' + device_role)
    logging.info('   Device Id: ' + device_id)
    logging.info('   Reachability: ' + device_reachable)
    logging.info('   Health: ' + str(device_health))
    logging.info('   Management IP Address: ' + device_management_ip_address)
    logging.info('   Serial Number: ' + device_serial_number)
    logging.info('   Family: ' + device_family)
    logging.info('   Software: ' + device_software)

    # retrieve device compliance
    logging.info('\n--------------------------------------------------------------------\n')
    logging.info(' Device Compliance Status')
    compliance_response = cc_api.compliance.compliance_details_of_device(device_uuid=device_id)
    compliance_status = compliance_response['response']
    # logging the device compliance
    for compliance in compliance_status:
        logging.info('    ' + compliance['complianceType'] + ' status: ' + compliance['status'])

    # execute suggested actions
    suggested_actions_response = cc_api.issues.execute_suggested_actions_commands(entity_type='issue_id', entity_value=issue_id)
    execution_id = suggested_actions_response['executionId']

    # check for execution to complete
    logging.info('\n--------------------------------------------------------------------\n')
    execution_status = 'IN_PROGRESS'
    logging.info(' Suggested actions execution started')
    time.sleep(10)
    while execution_status == 'IN_PROGRESS':
        execution_status_response = cc_api.task.get_business_api_execution_details(execution_id=execution_id)
        execution_status = execution_status_response['status']
        time.sleep(10)

    if execution_status != 'SUCCESS':
        logging.info(' Suggested actions execution failed')
    else:
        logging.info(' Suggested actions execution completed')
        suggested_actions_output = execution_status_response['bapiSyncResponse']
        status_json = json.loads(suggested_actions_output)

        # logging suggested actions executions
        for item in status_json:
            logging.info('\n...............................\n')
            logging.info('   ' + item['actionInfo'])
            logging.info('   Device: ' + item['hostname'])
            logging.info('   Command: ' + item['command'])
            command_output = item['commandOutput']
            output = command_output[item['command']]
            logging.info('   Command output: \n' + output)

        # knowledge base pull CLI commands and execution
        logging.info('\n--------------------------------------------------------------------\n')
        with open('troubleshooting_knowledgebase.yml', 'r') as file:
            knowledgebase = yaml.safe_load(file)

        # parse the input data
        cli_commands = knowledgebase[issue_name]['commands']
        logging.info(' Knowledgebase CLI commands:')
        for command in cli_commands:
            logging.info('    ' + command)
        logging.info('  ')

        # execute knowledge base commands
        command_runner_response = cc_api.command_runner.run_read_only_commands_on_devices(deviceUuids=[device_id], commands=cli_commands)
        logging.info(' Knowledgebase commands execution started')
        task_id = command_runner_response['response']['taskId']
        logging.info(' Task Id: ' + task_id)

        # check for task to complete
        end_time = ''
        time.sleep(1)
        while end_time == '':
            task_status_response = cc_api.task.get_task_by_id(task_id=task_id)['response']
            end_time = task_status_response['endTime']
            time.sleep(5)

        file_info = task_status_response['progress']
        logging.info(' Knowledgebase commands execution completed')
        file_info_json = json.loads(file_info)
        file_id = file_info_json['fileId']
        logging.info(' Commands output file Id: ' + file_id + '\n')

        # retrieve the commands output from file
        logging.info(' Knowledgebase CLI commands output:')
        file_content = cc_api.file.download_a_file_by_fileid(file_id=file_id).data
        file_content_data = file_content.decode('ASCII')
        file_content_json = json.loads(file_content_data)
        command_responses_success = file_content_json[0]['commandResponses']['SUCCESS']
        for key in command_responses_success:
            logging.info('\n...............................\n    ' + command_responses_success[key])

    current_time = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    logging.info(' App "Network Troubleshooting.py" run end, ' + current_time)


if __name__ == '__main__':
    main()
