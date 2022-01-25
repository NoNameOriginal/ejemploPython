from .. import db, app
from flask import render_template, request, jsonify
from ..models import Citas, Cuentas, Enfermeras, Ofertas, Pacientes, Secretarias, Sedes, Telefonos
from .ManejadorDeBaseDeDatos import *

CITAS="CITAS"
CUENTAS="CUENTAS"
ENFERMERAS="ENFERMERAS"
OFERTAS="OFERTAS"
PACIENTES="PACIENTES"
SECRETARIAS="SECRETARIAS"
SEDES="SEDES"
TELEFONOS="TELEFONOS"

def obtener_modelo(tabla):

    modelo: any
    modelo_esquema: any
    modelos_esquema: any

    if(tabla==CITAS):
        modelo = Citas.Citas
        modelo_esquema = Citas.CitasSchema()
        modelos_esquema = Citas.CitasSchema(many=True)
    if(tabla==CUENTAS):
        modelo = Cuentas.Cuentas
        modelo_esquema = Cuentas.CuentasSchema()
        modelos_esquema = Cuentas.CuentasSchema(many=True)
    if(tabla==ENFERMERAS):
        modelo = Enfermeras.Enfermeras
        modelo_esquema = Enfermeras.EnfermerasSchema()
        modelos_esquema = Enfermeras.EnfermerasSchema(many=True)
    if(tabla==OFERTAS):
        modelo = Ofertas.Ofertas
        modelo_esquema = Ofertas.OfertasSchema()
        modelos_esquema = Ofertas.OfertasSchema(many=True)
    if(tabla==PACIENTES):
        modelo = Pacientes.Pacientes
        modelo_esquema = Pacientes.PacientesSchema()
        modelos_esquema = Pacientes.PacientesSchema(many=True)
    if(tabla==SECRETARIAS):
        modelo = Secretarias.Secretarias
        modelo_esquema = Secretarias.SecretariasSchema()
        modelos_esquema = Secretarias.SecretariasSchema(many=True)
    if(tabla==SEDES):
        modelo = Sedes.Sedes
        modelo_esquema = Sedes.SedessSchema()
        modelos_esquema = Sedes.SedesSchema(many=True)
    if(tabla==TELEFONOS):
        modelo = Telefonos.Telefonos
        modelo_esquema = Telefonos.TelefonossSchema()
        modelos_esquema = Telefonos.TelefonosSchema(many=True)
    
    return modelo, modelo_esquema, modelos_esquema

@app.route('/')
def pagina_de_inicio():
    return render_template('index.html')

@app.route('/clientes')
def pagina_de_cliente():
    return render_template('clientes.html')

@app.route('/secretarias')
def pagina_de_secretaria():
    return render_template('secretarias.html')

@app.route('/login_cliente', methods=['POST'])
def login_cliente():

    cedula = request.form['cedula']
    contraseña = request.form['contraseña']

    modelo, modelo_esquema, modelos_esquemas = obtener_modelo(CUENTAS)
    informacion = obtener_fila(modelo, modelo_esquema, cedula)

    if(informacion is None):
        return render_template('clientes.html', error="Usuario no encontrado", isLogged=False)

    if(str(contraseña) == str(informacion.contrasegna)):
        modelo, modelo_esquema, modelos_esquemas = obtener_modelo(CITAS)
        citas = obtener_filas(modelo, modelos_esquemas)
        return render_template('clientes.html', citas=citas, isLogged=True)

    return render_template('clientes.html', error="Contraseña incorrecta", isLogged=False)

@app.route('/login_secretaria', methods=['POST'])
def login_secretaria():

    cedula = request.form['cedula']
    contraseña = request.form['contraseña']

    modelo, modelo_esquema, modelos_esquemas = obtener_modelo(CUENTAS)
    informacion = obtener_fila(modelo, modelo_esquema, cedula)

    if(informacion is None):
        return render_template('secretarias.html', error="Usuario no encontrado", isLogged=False)

    if(contraseña == informacion.contrasegna):
        modelo, modelo_esquema, modelos_esquemas = obtener_modelo(CITAS)
        citas = obtener_filas(modelo, modelos_esquemas)
        return render_template('secretarias.html', citas=citas, isLogged=True)
    if(contraseña == informacion.contrasegna):
        modelo, modelo_esquema, modelos_esquemas = obtener_modelo(ENFERMERAS)
        enfermeras = obtener_filas(modelo, modelos_esquemas)
        return render_template('secretarias.html', enfermeras=enfermeras, isLogged=True)
    if(contraseña == informacion.contrasegna):
        modelo, modelo_esquema, modelos_esquemas = obtener_modelo(OFERTAS)
        ofertas = obtener_filas(modelo, modelos_esquemas)
        return render_template('secretarias.html', ofertas=ofertas, isLogged=True)
    
    if(contraseña == informacion.contrasegna):
        modelo, modelo_esquema, modelos_esquemas = obtener_modelo(PACIENTES)
        pacientes = obtener_filas(modelo, modelos_esquemas)
        return render_template('secretarias.html', pacientes=pacientes, isLogged=True)
    
    if(contraseña == informacion.contrasegna):
        modelo, modelo_esquema, modelos_esquemas = obtener_modelo(SECRETARIAS)
        secretarias = obtener_filas(modelo, modelos_esquemas)
        return render_template('secretarias.html', secretarias=secretarias, isLogged=True)
    
    if(contraseña == informacion.contrasegna):
        modelo, modelo_esquema, modelos_esquemas = obtener_modelo(SEDES)
        sedes = obtener_filas(modelo, modelos_esquemas)
        return render_template('secretarias.html', sedes=sedes, isLogged=True)
    
    if(contraseña == informacion.contrasegna):
        modelo, modelo_esquema, modelos_esquemas = obtener_modelo(TELEFONOS)
        telefonos = obtener_filas(modelo, modelos_esquemas)
        return render_template('secretarias.html', telefonos=telefonos, isLogged=True)

    return render_template('secretarias.html', error="Contraseña incorrecta", isLogged=False)

@app.route('/modelos', methods=['POST'])
def create_user():

    tabla = request.json['tabla']
    datos = request.json['datos']

    modelo, modelo_esquema, modelos_esquemas = obtener_modelo(tabla)

    return crear_fila(modelo, modelo_esquema, dict(datos))


@app.route('/modelos', methods=['GET'])
def get_users():
    tabla = request.json['tabla']
    modelo, modelo_esquema, modelos_esquemas = obtener_modelo(tabla)
    return obtener_filas(modelo, modelos_esquemas)

@app.route('/modelos/<id>', methods=['GET'])
def get_user(id):
    tabla = request.json['tabla']
    modelo, modelo_esquema, modelos_esquemas = obtener_modelo(tabla)
    return obtener_fila(modelo, modelo_esquema, id)

@app.route('/modelos/<id>', methods=['PUT'])
def update_user(id):

    tabla = request.json['tabla']
    datos = request.json['datos']

    modelo, modelo_esquema, modelos_esquemas = obtener_modelo(tabla)

    return actualizar_fila(modelo, modelo_esquema, dict(datos), id)

@app.route('/modelos/<id>', methods=['DELETE'])
def delete_user(id):
    tabla = request.json['tabla']
    modelo, modelo_esquema, modelos_esquemas = obtener_modelo(tabla)
    return eliminar_fila(modelo, modelo_esquema, id)

db.create_all()