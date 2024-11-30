from jsonschema import validate, ValidationError

# Schema definition
assessment_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "assessment_id": {"type": "string"},
        "title": {"type": "string"},
        "description": {"type": "string"},
        "subject": {"type": "string"},
        "word_count": {"type": "integer"},
        "read_time": {"type": "string"},
        "publication_date": {
            "type": "string",
            "pattern": "^(\\d{4}/\\d{2}/\\d{2}|NA)$",
        },
        "details": {
            "type": "object",
            "properties": {
                "author": {"type": "string"},
                "difficulty_level": {"type": "string"},
                "keywords": {"type": "array", "items": {"type": "string"}},
            },
            "additionalProperties": True,
        },
    },
    "required": [
        "assessment_id",
        "title",
        "description",
        "subject",
        "word_count",
        "read_time",
        "publication_date",
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
