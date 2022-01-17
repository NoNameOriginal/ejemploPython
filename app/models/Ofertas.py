from . import *        
                       
class Ofertas(db.Model):
    __tablename__ = 'ofertas'
    id = db.Column(db.Integer, primary_key=True)
    precio = db.Column(db.Float)
    zona = db.Column(db.String(30))
    inicio = db.Column(db.Date)
    fin = db.Column(db.Date)
    paciente_cedula = db.Column(db.Integer, ForeignKey('pacientes.cedula'))
    citas_id = db.Column(db.Integer, ForeignKey('citas.id'))
    sede_id = db.Column(db.Integer, ForeignKey('sedes.id'))
    
    def __init__(self, idoferta, precio, zona, inicio, fin ):
        self.idoferta = idoferta 
        self.precio = precio
        self.zona = zona 
        self.inicio = inicio
        self.fin = fin

class OfertasSchema(ma.Schema):
    class Meta:
        fields = ('idoferta', 'precio', 'zona', 'inicio', 'fin')