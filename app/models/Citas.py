from . import *        
                    
class Citas(db.Model):
    __tablename__ = 'citas'
    id = db.Column(db.Integer, primary_key=True)
    dia = db.Column(db.Date)
    hora = db.Column(db.Time)
    zona = db.Column(db.String(30))
    duracion = db.Column(db.Time)
    oferta = relationship("ofertas", back_populates="citas")
    enfermeras_tarjetaProfesional = db.Column(db.Integer, ForeignKey('enfermeras.tarjetaProfesional'))
    paciente_cedula = db.Column(db.Integer, ForeignKey('pacientes.cedula'))
    sede_id = db.Column(db.Integer, ForeignKey('sedes.id'))

    def __init__(self, idcitas, dia, hora, zona, duracion ):
        self.idcitas = idcitas 
        self.dia = dia
        self.hora = hora
        self.zona = zona
        self.duracion = duracion

class CitasSchema(ma.Schema):
    class Meta:
        fields = ('dia', 'hora', 'zona', 'duracion')