from jsonrpc.JsonObject import json_object, json_field, validate_json_field

@json_object
class JsonRPCErrorObject:
    def __init__(self, code, message, data=None):
        super().__init__()

        self.code = code
        self.message = message
        self.data = data

    @json_field(name="code")
    def get_code(self):
        return self.code

    @staticmethod
    @validate_json_field("code")
    def validate_code(code):
        assert isinstance(code, int), "code should be an integer"

    @json_field("message")
    def get_message(self):
        return self.message

    @staticmethod
    @validate_json_field("message")
    def validate_message(message):
        assert isinstance(message, str), "message should be a short sentence"
