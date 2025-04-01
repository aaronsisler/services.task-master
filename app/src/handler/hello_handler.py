import json


def handle(event, _context):
    print(event)
    # 456

    return {"statusCode": 200, "body": json.dumps("Hello from Lambda!")}
