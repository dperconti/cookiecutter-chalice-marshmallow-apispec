from marshmallow import Schema, fields


class AliveSchema(Schema):
    """
    {
       "alive":"true"
    }
    """
    alive = fields.Boolean()
