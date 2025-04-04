from json import JSONEncoder


class ReceiptResponseEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
