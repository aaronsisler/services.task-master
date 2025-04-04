import json

from app.src.service import orchestration_service


def handle_delete(event, _context):
    print(event.get("queryStringParameters"))

    query_params: dict = event.get("queryStringParameters")
    
    if "stack_name" not in query_params:
        error_message = {"message": "Missing query param: stack_name"}
        return {"statusCode": 400, "body": json.dumps(error_message, indent=4)}

    return {"statusCode": 202, "body": json.dumps(query_params, indent=4)}

    # receipt_response: ReceiptResponse = cloudformation_stack_util.delete()
    # return {"statusCode": 202, "body": json.dumps(receipt_response, indent=4, cls=ResponseEncoder)}


def handle_create(event, _context):
    print(event)

    orchestration_service.orchestrate()

    return {"statusCode": 200, "body": json.dumps("Hello from Stack Handler: Create!")}
