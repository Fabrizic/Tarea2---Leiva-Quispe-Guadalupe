from utils.db import db
from dataclasses import dataclass

@dataclass
class Tipo_Predio(db.Model):
    id_tipo_predio: int
    nomre_predio: str
    
    id_tipo_predio=db.Column(db.Integer, primary_key=True)
    nomre_predio=db.Column(db.String(100))


    def __init__(self,id_tipo_predio,nomre_predio):
        self.id_tipo_predio=id_tipo_predio
        self.nomre_predio=nomre_predio