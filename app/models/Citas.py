from . import *        
                    
class Citas(db.Model):
    __tablename__ = 'citas'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date)
    hora = db.Column(db.Time)
    zona = db.Column(db.String(30))
    duracion = db.Column(db.Time)
    oferta = relationship("Ofertas", backref="citas")
    enfermeras_id = db.Column(db.Integer, ForeignKey('enfermeras.id'))
    paciente_id = db.Column(db.Integer, ForeignKey('pacientes.id'))
    sede_id = db.Column(db.Integer, ForeignKey('sedes.id'))

    def __init__(self, datadict ):
        for key, value in datadict.items():
            setattr(self, key, value)

class CitasSchema(ma.Schema):
    class Meta:
        fields = ('id','fecha', 'hora', 'zona')