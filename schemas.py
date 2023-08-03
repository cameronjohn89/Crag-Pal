from marshmallow import fields, Schema
from models.crag import Crag

class CragSchema(Schema):
    crag_id = fields.Integer()
    name = fields.String()
    location = fields.String()
    description = fields.String()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
