import json

from app.src.service import orchestration_service
from app.src.util import cloudformation_stack_util


def handle_delete(event, _context):
    print(event)

    receipt_response = cloudformation_stack_util.delete()

    return {"statusCode": 202, "body": json.dumps(receipt_response)}


def handle_create(event, _context):
    print(event)

    orchestration_service.orchestrate()

    return {"statusCode": 200, "body": json.dumps("Hello from Stack Handler: Create!")}
