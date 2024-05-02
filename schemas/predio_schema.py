from utils.ma import ma
from model.Predio import Predio
from marshmallow import fields
from schemas.tipo_predio_schema import TipoPredioSchema


class PredioSchema(ma.Schema):
    class Meta:
        model = Predio







        tipo_predio = ma.Nested(TipoPredioSchema)

predio_schema = PredioSchema()
predios_schema = PredioSchema(many = True)