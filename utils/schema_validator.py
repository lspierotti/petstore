import json
from jsonschema import validate, ValidationError
import os

def load_schema(schema_name):
    """Load a JSON schema from the schemas directory."""
    schema_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../schemas", schema_name)
    )
    print(f"Resolved schema path: {schema_path}")  # Debugging
    try:
        with open(schema_path, "r") as schema_file:
            return json.load(schema_file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Schema file not found: {schema_path}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in schema file: {schema_path}. Error: {e}")


def validate_json(json_data, schema_name):
    """Validate a JSON response against a schema."""
    schema = load_schema(schema_name)
    try:
        validate(instance=json_data, schema=schema)
    except ValidationError as e:
        raise AssertionError(f"JSON validation error: {e}")
