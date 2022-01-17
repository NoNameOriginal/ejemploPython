from . import *

class Sedes(db.Model):
    __tablename__ = 'sedes'
    id = db.Column(db.Integer, primary_key=True)
    centroComercial = db.Column(db.String(70))
    local = db.Column(db.Integer)
    horarioApertura = db.Column(db.Time)
    horarioCierre = db.Column(db.Time)
    telefonos = relationship("telefonos", back_populates="sede")
    secretaria = relationship("secretarias", back_populates="sede")
    enfermeras = relationship("enfermeras", back_populates="sede")
    citas = relationship("citas", back_populates="sede")
    oferta = relationship("ofertas", back_populates="sede")
    
    def __init__(self, centroComercial, local, horarioApertura,horarioCierre):
        self.centroComercial = centroComercial
        self.local = local
        self.horarioApertura = horarioApertura
        self.horarioCierre = horarioCierre

class SedesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'centroComercial', 'local', 'horarioApertura','horarioCierre')