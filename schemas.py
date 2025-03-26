from marshmallow import Schema, fields, validate

class ZeroShotRequestSchema(Schema):
    """
    Schema for zero-shot classification request
    """
    text = fields.String(required=True, validate=validate.Length(min=1, max=1000))
    labels = fields.List(
        fields.String(validate=validate.Length(min=1, max=100)),
        required=True,
        validate=validate.Length(min=1, max=10)
    )


