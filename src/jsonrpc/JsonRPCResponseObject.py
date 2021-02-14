from jsonrpc.JsonRPCObject import JsonRPCObject

class JsonRPCResponseObject(JsonRPCObject):
    def __init__(self, object_id ,result=None, error=None):
        super().__init__(object_id)

        self.result = result
        self.error = error

    def validate(self):
        super().validate()

        assert (self.result is not None) ^ (self.error is not None), "result or error should not be None."
