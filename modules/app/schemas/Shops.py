from jsonschema import validate
from jsonschema.exceptions import ValidationError
from jsonschema.exceptions import SchemaError

shop_schema = {
    "type":"object",
    "properties":{
        "id": {"type": "number"},
        "name": {"type":"string"},
        "products": {"type": "array"},
        "orders": {"type": "array"}
    },
    "required": ["id", "name", "products", "orders"],
    "additionalProperties": False
}

shop_update_schema = {
    "type":"object",
    "properties":{
        "id": {"type": "number"},
        "payload": {
            "type":"object",
            "properties":{
                "name": {"type":"string"},
                "products": {"type": "array"},
                "orders": {"type": "array"}
            },
            "additionalProperties": False
        }  
    },
    "required": ["id", "payload"],
    "additionalProperties": False
}

def validate_shop(data):
    try:
        validate(data, shop_schema)
    except ValidationError as e:
        return {'ok': False, 'message': e}
    except SchemaError as e:
        return {'ok': False, 'message': e}
    return {'ok': True, 'data': data}

def validate_shop_update(data):
    try:
        validate(data, shop_update_schema)
    except ValidationError as e:
        return {'ok': False, 'message': e}
    except SchemaError as e:
        return {'ok': False, 'message': e}
    return {'ok': True, 'data': data}