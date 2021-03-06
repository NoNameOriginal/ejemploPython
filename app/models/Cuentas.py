from . import *

class Cuentas(db.Model):
    __tablename__ = 'cuentas'
    cedula = db.Column(db.String(30), primary_key=True)
    contrasegna = db.Column(db.Integer)
    secretaria = relationship("Secretarias", backref="cuenta")
    paciente = relationship("Pacientes", backref="cuenta")
    
    def __init__(self, datadict ):
        for key, value in datadict.items():
            setattr(self, key, value)
    
class CuentasSchema(ma.Schema):
    class Meta:
        fields = ('cedula', 'contrasegna')
        