from . import *        
               
class Pacientes(db.Model):
    __tablename__ = 'pacientes'
    cedula = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30))
    apellidos = db.Column(db.String(45))
    citas = relationship("citas", back_populates="pacientes")
    oferta = relationship("ofertas", back_populates="pacientes")
    sede_id = db.Column(db.Integer, ForeignKey('sedes.id'))
    cuenta_usuario = db.Column(db.Integer, ForeignKey('cuentas.usuario'))
    
    def __init__(self, cedula, nombre, apellidos):
        self.cedula = cedula 
        self.nombre = nombre
        self.apeliidos = apellidos

class PacientesSchema(ma.Schema):
    class Meta:
        fields = ('cedula', 'nombre', 'apellidos')