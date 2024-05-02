from utils.ma import ma
from marshmallow import fields

class UbigeoSchema(ma.Schema):
    idubigeo = fields.Integer()
    departamento = fields.String()
    provincia = fields.String()
    distrito = fields.String()
    superficie = fields.Integer()
    altitud = fields.Integer()
    latitud = fields.Integer()
    longitud = fields.Integer()

ubigeo_schema = UbigeoSchema()
ubigeos_schema = UbigeoSchema(many=True)