import json

from app.src.service import orchestration_service


def handle(event, _context):
    print(event)

    orchestration_service.orchestrate()

    return {"statusCode": 200, "body": json.dumps("Hello from Stack Handler!")}
