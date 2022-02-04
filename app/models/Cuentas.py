from . import *

class Cuentas(db.Model):
    __tablename__ = 'cuentas'
    id = db.Column(db.Integer, primary_key=True)
    cedula = db.Column(db.Integer)
    contrasegna = db.Column(db.Integer)
    secretaria = relationship("Secretarias", backref="cuenta")
    paciente = relationship("Pacientes", backref="cuenta")
    
    def __init__(self, datadict ):
        for key, value in datadict.items():
            setattr(self, key, value)
    
class CuentasSchema(ma.Schema):
    class Meta:
        fields = ('id', 'cedula', 'contrasegna')
        