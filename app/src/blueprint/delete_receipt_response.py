class DeleteReceiptResponse:
    def __init__(self, stack_name, does_stack_exist=True, was_delete_triggered=False, error_message=None):
        super().__init__()
        self.stack_name = stack_name
        self.does_stack_exist = does_stack_exist
        self.was_delete_triggered = was_delete_triggered
        self.error_message = error_message

    @staticmethod
    def default(o):
        return o.__dict__
