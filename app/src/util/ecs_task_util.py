from operator import itemgetter

import boto3
from botocore.exceptions import ClientError


def find_latest_task_arn(task_name):
    try:
        client = boto3.client('ecs')

        response = client.describe_task_definition(taskDefinition=task_name)

        task_definition = itemgetter('taskDefinition')(response)

        if "taskDefinitionArn" not in task_definition:
            raise ClientError

        task_definition_arn = itemgetter('taskDefinitionArn')(task_definition)

        return task_definition_arn

    except ClientError as client_error:
        raise client_error
