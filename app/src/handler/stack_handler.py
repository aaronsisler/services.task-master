import json

from app.src.blueprint.receipt_response import ReceiptResponse
from app.src.blueprint.response_encoder import ResponseEncoder
from app.src.service import orchestration_service
from app.src.util import cloudformation_stack_util


def handle_delete(event, _context):
    print(event)

    receipt_response: ReceiptResponse = cloudformation_stack_util.delete()

    return {"statusCode": 202, "body": json.dumps(receipt_response, indent=4, cls=ResponseEncoder)}


def handle_create(event, _context):
    print(event)

    orchestration_service.orchestrate()

    return {"statusCode": 200, "body": json.dumps("Hello from Stack Handler: Create!")}
