import boto3
from botocore.exceptions import ClientError


def check_for_stack_existence(stack_name):
    try:
        client = boto3.client('cloudformation')
        data = client.describe_stacks(StackName=stack_name)
    except ClientError:
        return False

    return data['Stacks'][0]['StackStatus'] == 'CREATE_COMPLETE'


def delete_stack(stack_name):
    try:
        client = boto3.client('cloudformation')
        client.delete_stack(StackName=stack_name)
    except ClientError as client_error:
        raise client_error


def create_stack(stack_name, template_path, parameters, tags=None):
    if tags is None:
        tags = []
    try:
        client = boto3.client('cloudformation')

        client.create_stack(StackName=stack_name,
                            TemplateURL=template_path,
                            Parameters=parameters,
                            Tags=tags)
    except ClientError as client_error:
        raise client_error
