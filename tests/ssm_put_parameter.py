# Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

# https://docs.aws.amazon.com/code-samples/latest/catalog/python-ssm-ssm_put_parameter.py.html


import boto3
import logging
from botocore.exceptions import ClientError


def put_parameter(parameter_name, parameter_value, parameter_type, overwrite=False):
    """Creates new parameter in AWS SSM

    :param parameter_name: Name of the parameter to create in AWS SSM
    :param parameter_value: Value of the parameter to create in AWS SSM
    :param parameter_type: Type of the parameter to create in AWS SSM ('String'|'StringList'|'SecureString')
    :return: Return version of the parameter if successfully created else None
    """
    ssm_client = boto3.client('ssm')

    try:
        result = ssm_client.put_parameter(
            Name=parameter_name,
            Value=parameter_value,
            Type=parameter_type,
            Overwrite=overwrite
        )
        logging.info("%s was added to parameter store", parameter_name)
    except ClientError as e:
        logging.error(e)
        return None
    return result['Version']

def put_parameter_from_file(parameter_name, value_file, parameter_type, overwrite=False):
    """Creates new parameter in AWS SSM using contents of a file

    :param parameter_name: Name of the parameter to create in AWS SSM
    :param value_file: File which contains the value of the parameter to create in AWS SSM
    :param parameter_type: Type of the parameter to create in AWS SSM ('String'|'StringList'|'SecureString')
    :return: Return version of the parameter if successfully created else None
    """
    ssm_client = boto3.client('ssm')

    try:
        with open(value_file, 'r') as file:
            parameter_value = file.read()
            logging.info("value_file: %s" % value_file)
            logging.info(parameter_value)

        result = ssm_client.put_parameter(
            Name=parameter_name,
            Value=parameter_value,
            Type=parameter_type,
            Overwrite=overwrite
        )
        logging.info("%s was added to parameter store", parameter_name)
    except ClientError as e:
        logging.error(e)
        return None
    return result['Version']

def main():
    # Assign these values before running the program
    # If the specified specified parameter already exist in SSM, ParameterAlreadyExists error will be thrown
    parameter_name = 'test_param'
    parameter_value = 'test_value'
    parameter_type = 'String'  # ('String'|'StringList'|'SecureString')

    # Set up logging
    logging.basicConfig(level=logging.INFO,
                        format='%(levelname)s: %(asctime)s: %(message)s')
    result = put_parameter(parameter_name, parameter_value, parameter_type)
    logging.info(result)

    # using put parameter with overwrite,
    # If the specified parameter already exist a new version will be created
    result = put_parameter(parameter_name, parameter_value, parameter_type, overwrite=True)
    logging.info(result)

def main2():
#     parameter_name = 'test_param'
#     value_file = 'rsa_fake_test_key'
#     parameter_type = 'String'  # ('String'|'StringList'|'SecureString')

    parameter_name = '/etc/haproxy/private_test_key'
    value_file = 'rsa_fake_test_key'
    parameter_type = 'SecureString'  # ('String'|'StringList'|'SecureString')

    # Set up logging
    logging.basicConfig(level=logging.INFO,
                        format='%(levelname)s: %(asctime)s: %(message)s')
    result = put_parameter_from_file(parameter_name, value_file, parameter_type, overwrite=True)
    logging.info(result)

if __name__ == '__main__':
    main2()

