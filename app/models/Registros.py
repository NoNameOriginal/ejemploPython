from . import *

class Registros(db.Model):
    __tablename__ = 'registros'
    id = db.Column(db.Integer, primary_key=True)
    cedula = db.Column(db.String(30))
    nombre = db.Column(db.String(30))
    apellidos = db.Column(db.String(45))
    contrasegna = db.Column(db.Integer)
    celular = db.Column(db.String(45))
    email = db.Column(db.String(45))

    def __init__(self, datadict ):
        for key, value in datadict.items():
            setattr(self, key, value)

class RegistrosSchema(ma.Schema):
    class Meta:
        fields = ('id','cedula', 'nombre', 'apellidos','celular', 'email', 'contrasegna')