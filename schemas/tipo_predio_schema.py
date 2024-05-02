from utils.ma import ma
from marshmallow import fields

class TipoPredioSchema(ma.Schema):
    id_tipo_predio = fields.Integer()
    nomre_predio = fields.String()

TipoPredio_schema = TipoPredioSchema()
tiposPredio_schema = TipoPredioSchema(many=True)

