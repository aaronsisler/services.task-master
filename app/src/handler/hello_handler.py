import json


def handle(event, _context):
    print(event)

    return {"statusCode": 200, "body": json.dumps("Hello from Lambda!")}
