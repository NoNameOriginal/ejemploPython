from . import *        
        
class Secretarias(db.Model):
    __tablename__ = 'secretarias'
    cedula = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30))
    sede_id = db.Column(db.Integer, ForeignKey('sedes.id'))
    cuenta_usuario = db.Column(db.Integer, ForeignKey('cuentas.usuario'))
    
    def __init__(self, datadict ):
        for key, value in datadict.items():
            setattr(self, key, value)

class SecretariasSchema(ma.Schema):
    class Meta:
        fields = ('cedulaSecre', 'nombreSecre')