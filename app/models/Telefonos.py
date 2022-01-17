from . import *

class Telefonos(db.Model):
    __tablename__ = 'telefonos'
    telefono = db.Column(db.Integer, primary_key=True)
    sede_id = db.Column(db.Integer, ForeignKey('sedes.id'))
    
    def __init__(self, telefonos, sede_id):
        self.telefonos = telefonos 
        self.sede_id = sede_id
    
class TelefonosSchema(ma.Schema):
    class Meta:
        fields = ('telefonos', 'sede_id')