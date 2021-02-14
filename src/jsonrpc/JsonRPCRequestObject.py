from jsonrpc.JsonRPCObject import JsonRPCObject, json_object, json_field, validate_json_field

@json_object
class JsonRPCRequestObject(JsonRPCObject):
    def __init__(self, object_id, method, params):
        super().__init__(object_id)

        self.method = method
        self.params = params

    def validate(self):
        super().validate()


    @json_field("params")
    def get_params(self):
        return self.params

    @staticmethod
    @validate_json_field("method")
    def validate_method(method):
        assert isinstance(method, str), "method should be a string."

    @json_field("method")
    def get_method(self):
        return self.method

    @staticmethod
    @validate_json_field("params")
    def validate_params(params):
        assert params is None or hasattr(params, "_json_fields"), "params should be omitted or a Json structure."
