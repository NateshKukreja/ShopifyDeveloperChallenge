from jsonschema import validate
from jsonschema.exceptions import ValidationError
from jsonschema.exceptions import SchemaError


lineSchema = {
    "type":"object",
    "properties":{
        "quantity": {"type": "number"},
        "price": {"type":"number"},
    },
    "required": ["quantity", "price", "product"],
    "additionalProperties": false
}