import boto3
from botocore.exceptions import ClientError

from app.src.blueprint.create_receipt_response import CreateReceiptResponse
from app.src.blueprint.delete_receipt_response import DeleteReceiptResponse


def create(stack_name):
    does_stack_exist = __stack_exists(stack_name)

    if does_stack_exist:
        return CreateReceiptResponse(stack_name=stack_name,
                                     does_stack_exist=does_stack_exist)
    return None


def delete(stack_name):
    does_stack_exist = __stack_exists(stack_name)

    if not does_stack_exist:
        return DeleteReceiptResponse(stack_name=stack_name,
                                     does_stack_exist=does_stack_exist,
                                     was_delete_triggered=False)
    try:
        __delete_stack(stack_name)

        return DeleteReceiptResponse(stack_name=stack_name,
                                     does_stack_exist=True,
                                     was_delete_triggered=True)

    except ClientError as client_error:
        return DeleteReceiptResponse(stack_name=stack_name,
                                     does_stack_exist=True,
                                     was_delete_triggered=False,
                                     error_message=client_error)


def __stack_exists(stack_name, required_status='CREATE_COMPLETE'):
    try:
        client = boto3.client('cloudformation')
        data = client.describe_stacks(StackName=stack_name)
    except ClientError:
        return False

    return data['Stacks'][0]['StackStatus'] == required_status


def __delete_stack(stack_name):
    try:
        client = boto3.client('cloudformation')
        client.delete_stack(StackName=stack_name)
    except ClientError as client_error:
        raise client_error


def __create_stack(stack_name):
    try:
        client = boto3.client('cloudformation')
        client.create_stack(StackName=stack_name)
    except ClientError as client_error:
        raise client_error
