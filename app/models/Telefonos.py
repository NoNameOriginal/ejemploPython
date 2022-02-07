from . import *

class Telefonos(db.Model):
    __tablename__ = 'telefonos'
    id = db.Column(db.String(30), primary_key=True)
    telefono = db.Column(db.String(30))
    sede_id = db.Column(db.String(30), ForeignKey('sedes.id'))
    
    def __init__(self, datadict ):
        for key, value in datadict.items():
            setattr(self, key, value)

class TelefonosSchema(ma.Schema):
    class Meta:
        fields = ('id','telefono', 'sede_id')