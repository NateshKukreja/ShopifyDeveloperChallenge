from jsonschema import validate
from jsonschema.exceptions import ValidationError
from jsonschema.exceptions import SchemaError

shopSchema = {
    "type":"object",
    "properties":{
        "id": {"type": "number"},
        "name": {"type":"string"},
        "products": {
            "type": "array",
            "items": {"$ref": "products_schema.json"}
        },
        "orders": {
            "type": "array",
            "items":{"$ref": "orders_schema.json"}
        }
    },
    "required": ["id", "name", "products", "orders"],
    "additionalProperties": false
}

def validate_shop(data):
    try:
        validate(data, 'JSON/shop_schema.json')
    except ValidationError as e:
        return {'ok': False, 'message': e}
    except SchemaError as e:
        return {'ok': False, 'message': e}
    return {'ok': True, 'data': data}

def validate_shop_update(data):
    try:
        validate(data, 'JSON/shop_update_schema.json')
    except ValidationError as e:
        return {'ok': False, 'message': e}
    except SchemaError as e:
        return {'ok': False, 'message': e}
    return {'ok': True, 'data': data}