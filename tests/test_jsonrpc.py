import unittest
from jsonrpc.JsonRPCErrorObject import JsonRPCErrorObject
from jsonrpc.JsonRPCRequestObject import JsonRPCRequestObject
from jsonrpc.JsonObject import validate, export
import json

class TestJsonRPC(unittest.TestCase):
    def test_json_validation(self):
        json_error = JsonRPCErrorObject(12, "Standard error.")
        validate(json_error)

        with self.assertRaises(Exception) as context:
            json_error = JsonRPCErrorObject("toto", 12)
            validate(json_error)

        self.assertTrue("JsonRPCError should raise an Exception if code field is not an int.")

        jsonrpc_request = JsonRPCRequestObject(0, "Call", None)
        validate(jsonrpc_request)

    def test_json_export(self):
        json_error = JsonRPCErrorObject(0, "No error.")
        json_string = export(json_error)

        jsonrpc_request = JsonRPCRequestObject(0, "Fold", None)
        json_string = export(jsonrpc_request)


if __name__ == '__main__':
    unittest.main()
