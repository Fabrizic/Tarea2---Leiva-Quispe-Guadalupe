from utils.ma import ma
from model.predio import Predio
from marshmallow import fields
from schemas.tipo_predio_schema import TipoPredioSchema

class PredioSchema(ma.Schema):
    class Meta:
        model  = Predio
        fields = ('id_predio',
                  'id_tipo_predio',
                  'descripcion',
                  'ruc',
                  'telefono',
                  'correo',
                  'direccion',
                  'idubigeo',
                  'id_persona',
                  'url_imagen',
                  'total_mdu',
                  'tipo_predio')
    
    tipo_predio = ma.Nested(TipoPredioSchema)    

predio_schema = PredioSchema()
predios_schema = PredioSchema(many=True)