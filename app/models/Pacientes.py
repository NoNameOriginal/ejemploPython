from . import *        
               
class Pacientes(db.Model):
    __tablename__ = 'pacientes'
    cedula = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30))
    apellidos = db.Column(db.String(45))
    citas = relationship("Citas", backref="pacientes")
    oferta = relationship("Ofertas", backref="pacientes")
    sede_id = db.Column(db.Integer, ForeignKey('sedes.id'))
    cuenta_usuario = db.Column(db.Integer, ForeignKey('cuentas.cedula'))
    
    def __init__(self, datadict ):
        for key, value in datadict.items():
            setattr(self, key, value)

class PacientesSchema(ma.Schema):
    class Meta:
        fields = ('cedula', 'nombre', 'apellidos','sede_id')