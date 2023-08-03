from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.crag import Crag

class CragSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Crag