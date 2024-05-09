from utils.ma import ma
from model.Predio import Predio
from marshmallow import fields
from schemas.tipo_predio_schema import TipoPredioSchema
from schemas.persona_schema import PersonaSchema
from schemas.ubigeo_schema import UbigeoSchema

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
                  'tipo_predio',
                  'ubigeo',
                  'persona')
    
    tipo_predio = ma.Nested(TipoPredioSchema)
    ubigeo = ma.Nested(UbigeoSchema)
    persona = ma.Nested(PersonaSchema)    

predio_schema = PredioSchema()
predios_schema = PredioSchema(many=True)