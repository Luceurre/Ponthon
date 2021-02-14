from jsonrpc.JsonObject import json_object, json_field, validate_json_field

JSONRPC_VERSION = "2.0"

class JsonRPCBaseObject:
    pass

class JsonRPCObject(JsonRPCBaseObject):
    def __init__(self, object_id, jsonrpc=JSONRPC_VERSION):
        super().__init__()

        self.jsonrpc = jsonrpc
        self.object_id = object_id

    @json_field("jsonrpc")
    def get_jsonrpc(self):
        return self.jsonrpc

    @json_field("id")
    def get_id(self):
        return self.object_id

    @staticmethod
    @validate_json_field("jsonrpc")
    def validate_jsonrpc(jsonrpc):
        assert jsonrpc == JSONRPC_VERSION, f"jsonrpc field should be {JSONRPC_VERSION}"

    @staticmethod
    @validate_json_field("id")
    def validate_id(object_id):
        try:
            int(object_id)
        except TypeError:
            raise TypeError("id should be a string or an int")

    def validate(self):
        super().validate()

