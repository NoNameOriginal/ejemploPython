from . import *        
               
class Enfermeras(db.Model):
    __tablename__ = 'enfermeras'
    tarjetaProfesional = db.Column(db.Integer, primary_key=True)
    cedula = db.Column(db.Integer)
    nombre = db.Column(db.String(30))
    citas = relationship("Citas", backref="enfermeras")
    sede_id = db.Column(db.Integer, ForeignKey('sedes.id'))
    
    def __init__(self, datadict ):
        for key, value in datadict.items():
            setattr(self, key, value)

class EnfermerasSchema(ma.Schema):
    class Meta:
        fields = ('tarjetaProfesional', 'cedula', 'nombre', 'sede_id')