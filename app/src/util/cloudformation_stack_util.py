from app.src.blueprint.receipt_response import ReceiptResponse


def create():
    return True


def delete():
    return ReceiptResponse(stack_id="this is a stack id")
