from jsonschema import validate, ValidationError

# Schema definition
assessment_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "assessment_id": {"type": "string"},
        "title": {"type": "string", "minLength": 1},
        "description": {"type": "string"},
        "subject": {"type": "string", "minLength": 1},
        "word_count": {"type": "integer", "minimum": 0},
        "read_time": {"type": "string"},
        "publication_date": {
            "type": "string",
            "pattern": "^(\\d{4}/\\d{2}/\\d{2}|NA)$",  # YYYY/MM/DD or 'NA'
        },
        "details": {"type": "array", "items": {"type": "string"}, "default": []},
    },
    "required": [
        "assessment_id",
        "title",
        "description",
        "subject",
        "word_count",
        "read_time",
        "publication_date",
        "details",
    ],
    "additionalProperties": False,
}


def validate_assessment(data):
    try:
        validate(instance=data, schema=assessment_schema)
        return True
    except ValidationError as e:
        print(f"Validation Error: {e.message}")
        return False
