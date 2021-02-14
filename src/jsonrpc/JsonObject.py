import numbers
import json

def json_object(cls):
    """Class decorator. Decorated class can be exported to json."""
    cls._json_fields = {}
    cls._validate_json_fields = {}

    for methodname in dir(cls):
        method = getattr(cls, methodname)
        if hasattr(method, '_json_field'):
            field_name = method._json_field
            cls._json_fields[field_name] = method

        if hasattr(method, '_validate_json_field'):
            field_name = method._validate_json_field
            cls._validate_json_fields[field_name] = method

    for json_field in cls._json_fields.keys():
        if not cls._validate_json_fields.get(json_field, None):
            print(f"[WARNING] {json_field} has no validation for {cls.__name__}.")
    return cls

def json_field(name):
    def decorator(field):
        """Decorator to add a field to the exported json."""
        field._json_field = name
        return field
    return decorator

def validate_json_field(name):
    """Decorator to add a validation function to a given field."""
    def decorator(validate_field):
        validate_field._validate_json_field = name
        return validate_field

    return decorator

def validate(json_object):
        """Check if current object is a valid JSONRPC Object.
        Throw error otherwise."""

        json_fields = json_object._json_fields
        validate_json_fields = json_object._validate_json_fields


        for field_name in json_fields.keys():
            validator = validate_json_fields.get(field_name, None)
            field_value = json_fields[field_name](json_object)

            if validator is not None:
                validator(field_value)

def format_string(string):
    return f"\"{string}\""

def export_value(field_value):
    json_value = ""
    is_number = isinstance(field_value, numbers.Number)
    if is_number:
        json_value += f": {field_value}"

    is_string = isinstance(field_value, str)
    if is_string:
        json_value += f": {format_string(field_value)}"

    is_list = isinstance(field_value, list)
    if is_list:
        json_value += "["

        for value in field_value:
            json_value += export_value(value) + ","
        json_value += "]"
    return json_value

def export(json_object):
    """Return a string containing a valid JSON object with object data."""

    if not hasattr(json_object, "_json_fields"):
        return json.dumps(json_object)
    validate(json_object)
    json_fields = json_object._json_fields

    json_dict = {}
    for field_name in json_fields.keys():
        field_value = json_fields[field_name](json_object)
        json_dict[field_name] = export(field_value)

    return json.dumps(json_dict)
