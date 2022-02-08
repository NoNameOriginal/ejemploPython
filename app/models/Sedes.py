from . import *

class Sedes(db.Model):
    __tablename__ = 'sedes'
    id = db.Column(db.Integer, primary_key=True)
    centroComercial = db.Column(db.String(70))
    local = db.Column(db.Integer)
    horarioApertura = db.Column(db.Time)
    horarioCierre = db.Column(db.Time)
    telefonos = relationship("Telefonos", backref="sede")
    secretaria = relationship("Secretarias", backref="sede")
    enfermeras = relationship("Enfermeras", backref="sede")
    citas = relationship("Citas", backref="sede")
    oferta = relationship("Ofertas", backref="sede")
    
    def __init__(self, datadict ):
        for key, value in datadict.items():
            setattr(self, key, value)

class SedesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'centroComercial', 'local', 'horarioApertura','horarioCierre')