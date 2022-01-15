from .. import db, ma

class Sede(db.Model):
    __tablename__ = 'sede'
    id = db.Column(db.Integer, primary_key=True)
    centroComercial = db.Column(db.String(70))
    local = db.Column(db.Integer)
    horarioApertura = db.Column(db.Time)
    horarioCierre = db.Column(db.Time)
    telefonos = relationship("telefonos", back_populates="sede")
    secretaria = relationship("secretaria", back_populates="sede")
    enfermeras = relationship("enfermeras", back_populates="sede")
    citas = relationship("citas", back_populates="sede")
    oferta = relationship("oferta", back_populates="sede")
    
    def __init__(self, centroComercial, local, horarioApertura,horarioCierre):
        self.centroComercial = centroComercial
        self.local = local
        self.horarioApertura = horarioApertura
        self.horarioCierre = horarioCierre

class SedeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'centroComercial', 'local', 'horarioApertura','horarioCierre')
        

class Telefonos(db.Model):
    __tablename__ = 'telefonos'
    telefonos = db.Column(db.Integer(10), primary_key=True)
    sede_id = db.Column(db.Integer, ForeignKey('sede.id'))
    
    def __init__(self, telefonos, sede_id):
        self.telefonos = telefonos 
        self.sede_id = sede_id
        
class TelefonosSchema(ma.Schema):
    class Meta:
        fields = ('telefonos', 'sede_id')


class Cuenta(db.Model):
    __tablename__ = 'cuenta'
    usuario = db.Column(db.Integer(10), primary_key=True)
    contraseña = db.Column(db.Integer(4))
    secretaria = relationship("secretaria", back_populates="cuenta")
    paciente = relationship("secretaria", back_populates="cuenta")
    
    def __init__(self, usuario, contraseña):
        self.usuario = usuario 
        self.contraseña = contraseña
        
class CuentaSchema(ma.Schema):
    class Meta:
        fields = ('usuario', 'contraseña')
        
        
class Secretaria(db.Model):
    __tablename__ = 'secretaria'
    cedulaSecre = db.Column(db.Integer(10), primary_key=True)
    nombreSecre = db.Column(db.String(30))
    sede_id = db.Column(db.Integer, ForeignKey('sede.id'))
    cuenta_secre = db.Column(db.Integer, ForeignKey('cuenta.usuario'))
    
    def __init__(self, cedulaSecre, nombreSecre):
        self.cedulaSecre = cedulaSecre 
        self.nombreSecre = nombreSecre

class SecretariaSchema(ma.Schema):
    class Meta:
        fields = ('cedulaSecre', 'nombreSecre')
        

class Paciente(db.Model):
    __tablename__ = 'paciente'
    cedula = db.Column(db.Integer(10), primary_key=True)
    nombre = db.Column(db.String(30))
    apellidos = db.Column(db.String(45))
    citas = relationship("citas", back_populates="pacientes")
    oferta = relationship("oferta", back_populates="pacientes")
    sede_id = db.Column(db.Integer, ForeignKey('sede.id'))
    cuenta_usuario = db.Column(db.Integer, ForeignKey('cuenta.usuario'))
    
    def __init__(self, cedula, nombre, apellidos):
        self.cedula = cedula 
        self.nombre = nombre
        self.apeliidos = apellidos

class PacienteSchema(ma.Schema):
    class Meta:
        fields = ('cedula', 'nombre', 'apellidos')
        

class Enfermeras(db.Model):
    __tablename__ = 'enfermeras'
    tarjetaProfesional = db.Column(db.Integer(20), primary_key=True)
    cedulaEnfer = db.Column(db.Integer(10))
    nombre = db.Column(db.String(30))
    citas = relationship("citas", back_populates="enfermeras")
    sede_id = db.Column(db.Integer, ForeignKey('sede.id'))
    
    def __init__(self, tarjetaProfesional, cedulaEnfer, nombre):
        self.tarjetaProfesional = tarjetaProfesional 
        self.cedulaEnfer = cedulaEnfer
        self.nombre = nombre

class EnfermerasSchema(ma.Schema):
    class Meta:
        fields = ('tarjetaProfesional', 'cedulaEnfer', 'nombre')
        
class Citas(db.Model):
    __tablename__ = 'citas'
    idcitas = db.Column(db.Integer, primary_key=True)
    dia = db.Column(db.Date)
    hora = db.Column(db.Time)
    zona = db.Column(db.String(30))
    duracion = db.Column(db.Time)
    oferta = relationship("oferta", back_populates="citas")
    enfermeras_tarjetaProfesional = db.Column(db.Integer, ForeignKey('enfermeras.tarjetaProfesional'))
    paciente_cedula = db.Column(db.Integer, ForeignKey('paciente.cedula'))
    sede_id = db.Column(db.Integer, ForeignKey('sede.id'))

    def __init__(self, idcitas, dia, hora, zona, duracion ):
        self.idcitas = idcitas 
        self.dia = dia
        self.hora = hora
        self.zona = zona
        self.duracion = duracion
        
class CitasSchema(ma.Schema):
    class Meta:
        fields = ('idcitas', 'dia', 'hora', 'zona', 'duracion')
        

class Oferta(db.Model):
    __tablename__ = 'oferta'
    idoferta = db.Column(db.Integer, primary_key=True)
    precio = db.Column(db.Enum)
    zona = db.Column(db.String(30))
    inicio = db.Column(db.Date)
    fin = db.Column(db.Date)
    paciente_cedula = db.Column(db.Integer, ForeignKey('paciente.cedula'))
    citas_id = db.Column(db.Integer, ForeignKey('citas.idcitas'))
    sede_id = db.Column(db.Integer, ForeignKey('sede.id'))
    
    def __init__(self, idoferta, precio, zona, inicio, fin ):
        self.idoferta = idoferta 
        self.precio = precio
        self.zona = zona 
        self.inicio = inicio
        self.fin = fin

class OfertaSchema(ma.Schema):
    class Meta:
        fields = ('idoferta', 'precio', 'zona', 'inicio', 'fin')