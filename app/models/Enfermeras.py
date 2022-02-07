from . import *        
               
class Enfermeras(db.Model):
    __tablename__ = 'enfermeras'
    id = db.Column(db.String(30), primary_key=True)
    tarjetaProfesional = db.Column(db.String(30))
    cedula = db.Column(db.String(30))
    nombre = db.Column(db.String(30))
    citas = relationship("Citas", backref="enfermeras")
    sede_id = db.Column(db.String(30), ForeignKey('sedes.id'))
    
    def __init__(self, datadict ):
        for key, value in datadict.items():
            setattr(self, key, value)

class EnfermerasSchema(ma.Schema):
    class Meta:
        fields = ('id','tarjetaProfesional', 'cedula', 'nombre', 'sede_id')