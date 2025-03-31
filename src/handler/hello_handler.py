import json


def hello_handler(event, context):

    print(event)

    return {"statusCode": 200, "body": json.dumps("Hello from Lambda!")}
