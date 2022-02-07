from . import *        
        
class Secretarias(db.Model):
    __tablename__ = 'secretarias'
    id = db.Column(db.String(30), primary_key=True)
    cedula = db.Column(db.String(30))
    nombre = db.Column(db.String(30))
    sede_id = db.Column(db.String(30), ForeignKey('sedes.id'))
    cuenta_usuario = db.Column(db.String(30), ForeignKey('cuentas.cedula'))
    
    def __init__(self, datadict ):
        for key, value in datadict.items():
            setattr(self, key, value)

class SecretariasSchema(ma.Schema):
    class Meta:
        fields = ('id','cedula', 'nombre','sede_id')