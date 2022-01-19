from . import *

class Cuentas(db.Model):
    __tablename__ = 'cuentas'
    usuario = db.Column(db.Integer, primary_key=True)
    contraseña = db.Column(db.Integer)
    secretaria = relationship("Secretarias", backref="cuenta")
    paciente = relationship("Pacientes", backref="cuenta")
    
    def __init__(self, datadict ):
        for key, value in datadict.items():
            setattr(self, key, value)
    
class CuentasSchema(ma.Schema):
    class Meta:
        fields = ('usuario', 'contraseña')
        