import json

from app.src.blueprint.create_receipt_response import CreateReceiptResponse
from app.src.blueprint.create_stack_request import CreateStackRequest
from app.src.blueprint.delete_receipt_response import DeleteReceiptResponse
from app.src.blueprint.response_encoder import ResponseEncoder
from app.src.service import orchestration_service


def handle_create(event, _context):
    body_content: dict = json.loads(event.get("body"))

    if "service_name" not in body_content:
        error_message = {"message": "Missing body attribute: service_name"}
        return {"statusCode": 400, "body": json.dumps(error_message, indent=4)}

    if "dns_prefix" not in body_content:
        error_message = {"message": "Missing body attribute: dns_prefix"}
        return {"statusCode": 400, "body": json.dumps(error_message, indent=4)}

    if "cost_center_tag" not in body_content:
        error_message = {"message": "Missing body attribute: cost_center_tag"}
        return {"statusCode": 400, "body": json.dumps(error_message, indent=4)}

    create_stack_request: CreateStackRequest = CreateStackRequest(body_content.get("service_name"),
                                                                  body_content.get("dns_prefix"),
                                                                  body_content.get("cost_center_tag")
                                                                  )

    receipt_response: CreateReceiptResponse = orchestration_service.create_stack(create_stack_request)

    if receipt_response.error_message is not None:
        return {"statusCode": 500, "body": json.dumps(receipt_response, indent=4, cls=ResponseEncoder)}

    return {"statusCode": 202, "body": json.dumps(receipt_response, indent=4, cls=ResponseEncoder)}


def handle_delete(event, _context):
    query_params: dict = event.get("queryStringParameters")

    if "stack_name" not in query_params:
        error_message = {"message": "Missing query param: stack_name"}
        return {"statusCode": 400, "body": json.dumps(error_message, indent=4)}

    stack_name = query_params.get("stack_name")

    receipt_response: DeleteReceiptResponse = orchestration_service.delete_stack(stack_name)

    if receipt_response.error_message is not None:
        return {"statusCode": 500, "body": json.dumps(receipt_response, indent=4, cls=ResponseEncoder)}

    return {"statusCode": 202, "body": json.dumps(receipt_response, indent=4, cls=ResponseEncoder)}
