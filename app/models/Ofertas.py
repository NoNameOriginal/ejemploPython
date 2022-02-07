from . import *        
                       
class Ofertas(db.Model):
    __tablename__ = 'ofertas'
    id = db.Column(db.String(30), primary_key=True)
    precio = db.Column(db.Float)
    zona = db.Column(db.String(30))
    inicio = db.Column(db.Date)
    fin = db.Column(db.Date)
    paciente_cedula = db.Column(db.String(30), ForeignKey('pacientes.cedula'))
    citas_id = db.Column(db.String(30), ForeignKey('citas.id'))
    sede_id = db.Column(db.String(30), ForeignKey('sedes.id'))
    
    def __init__(self, datadict ):
        for key, value in datadict.items():
            setattr(self, key, value)

class OfertasSchema(ma.Schema):
    class Meta:
        fields = ('id', 'precio', 'zona', 'inicio', 'fin','paciente_cedula','citas_id', 'sede_id')