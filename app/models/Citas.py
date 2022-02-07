from . import *        
                    
class Citas(db.Model):
    __tablename__ = 'citas'
    id = db.Column(db.String(30), primary_key=True)
    fecha = db.Column(db.Date)
    hora = db.Column(db.Time)
    zona = db.Column(db.String(30))
    duracion = db.Column(db.Time)
    oferta = relationship("Ofertas", backref="citas")
    enfermeras_tarjetaProfesional = db.Column(db.String(30), ForeignKey('enfermeras.tarjetaProfesional'))
    paciente_cedula = db.Column(db.String(30), ForeignKey('pacientes.cedula'))
    sede_id = db.Column(db.String(30), ForeignKey('sedes.id'))

    def __init__(self, datadict ):
        for key, value in datadict.items():
            setattr(self, key, value)

class CitasSchema(ma.Schema):
    class Meta:
        fields = ('id','fecha', 'hora', 'zona', 'duracion')