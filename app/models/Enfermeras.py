from . import *        
               
class Enfermeras(db.Model):
    __tablename__ = 'enfermeras'
    tarjetaProfesional = db.Column(db.Integer, primary_key=True)
    cedula = db.Column(db.Integer)
    nombre = db.Column(db.String(30))
    citas = relationship("citas", back_populates="enfermeras")
    sede_id = db.Column(db.Integer, ForeignKey('sedes.id'))
    
    def __init__(self, tarjetaProfesional, cedulaEnfer, nombre):
        self.tarjetaProfesional = tarjetaProfesional 
        self.cedulaEnfer = cedulaEnfer
        self.nombre = nombre

class EnfermerasSchema(ma.Schema):
    class Meta:
        fields = ('tarjetaProfesional', 'cedulaEnfer', 'nombre')