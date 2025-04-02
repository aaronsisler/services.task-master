import json


def handle(event, _context):
    print(event)
    # Rawr

    return {"statusCode": 200, "body": json.dumps("Hello from Stack Handler!")}
