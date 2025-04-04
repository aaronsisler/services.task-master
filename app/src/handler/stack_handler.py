import json

from app.src.blueprint.delete_receipt_response import DeleteReceiptResponse
from app.src.blueprint.response_encoder import ResponseEncoder
from app.src.service import orchestration_service
from app.src.util import cloudformation_stack_util


def handle_delete(event, _context):
    print(event.get("queryStringParameters"))

    query_params: dict = event.get("queryStringParameters")

    if "stack_name" not in query_params:
        error_message = {"message": "Missing query param: stack_name"}
        return {"statusCode": 400, "body": json.dumps(error_message, indent=4)}

    stack_name = query_params.get("stack_name")

    receipt_response: DeleteReceiptResponse = cloudformation_stack_util.delete(stack_name)

    return {"statusCode": 202, "body": json.dumps(receipt_response, indent=4, cls=ResponseEncoder)}


def handle_create(event, _context):
    print(event)

    orchestration_service.orchestrate()

    return {"statusCode": 200, "body": json.dumps("Hello from Stack Handler: Create!")}
