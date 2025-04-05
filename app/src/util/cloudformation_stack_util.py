import json

import boto3
from botocore.exceptions import ClientError


def check_for_stack_existence(stack_name):
    try:
        client = boto3.client('cloudformation')
        # If stack doesn't exist, client will throw ClientError
        client.describe_stacks(StackName=stack_name)
        return True
    except ClientError:
        return False


def delete_stack(stack_name):
    try:
        client = boto3.client('cloudformation')
        client.delete_stack(StackName=stack_name)
    except ClientError as client_error:
        raise client_error


def create_stack(stack_name, template_content, parameters, tags=None):
    if tags is None:
        tags = []
    try:
        client = boto3.client('cloudformation')

        client.create_stack(StackName=stack_name,
                            TemplateBody=json.dumps(template_content),
                            Parameters=parameters,
                            Tags=tags)
    except ClientError as client_error:
        raise client_error
