class CreateReceiptResponse:
    def __init__(self, stack_name, stack_id=None, does_stack_exist=False, was_create_triggered=False,
                 error_message=None):
        super().__init__()
        self.stack_name = stack_name
        self.stack_id = stack_id
        self.does_stack_exist = does_stack_exist
        self.was_create_triggered = was_create_triggered
        self.error_message = error_message

    @staticmethod
    def default(o):
        return o.__dict__
