import boto3
from botocore.exceptions import ClientError

from app.src.blueprint.receipt_response import ReceiptResponse


def create():
    return True


def delete(stack_name):
    does_stack_exist = __stack_exists(stack_name)
    print("does_stack_exist")
    print(does_stack_exist)
    return ReceiptResponse(stack_id=stack_name, does_stack_exist=does_stack_exist)


def __stack_exists(name, required_status='CREATE_COMPLETE'):
    try:
        client = boto3.client('cloudformation')
        data = client.describe_stacks(StackName=name)
    except ClientError:
        return False

    return data['Stacks'][0]['StackStatus'] == required_status
