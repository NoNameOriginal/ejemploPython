from . import *

class Cuentas(db.Model):
    __tablename__ = 'cuentas'
    usuario = db.Column(db.Integer, primary_key=True)
    contraseña = db.Column(db.Integer)
    secretaria = relationship("secretarias", back_populates="cuenta")
    paciente = relationship("pacientes", back_populates="cuenta")
    
    def __init__(self, usuario, contraseña):
        self.usuario = usuario 
        self.contraseña = contraseña
    
class CuentasSchema(ma.Schema):
    class Meta:
        fields = ('usuario', 'contraseña')
        