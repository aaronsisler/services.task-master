from json import JSONEncoder


class ReceiptResponse(JSONEncoder):
    def __init__(self, stack_id):
        super().__init__()
        self.stack_id = stack_id

    def default(self, o):
        return o.__dict__
