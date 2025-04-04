class ReceiptResponse:
    def __init__(self, stack_id, does_stack_exist):
        super().__init__()
        self.stack_id = stack_id
        self.does_stack_exist = does_stack_exist

    def default(self, o):
        return o.__dict__
