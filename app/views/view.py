from pickletools import read_uint1
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
        modelo_esquema = Sedes.SedesSchema()
        modelos_esquema = Sedes.SedesSchema(many=True)
    if(tabla==TELEFONOS):
        modelo = Telefonos.Telefonos
        modelo_esquema = Telefonos.TelefonosSchema()
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

    if(str(contraseña) != str(informacion.contrasegna)):
        return render_template('secretarias.html', error="Contraseña incorrecta", isLogged=False)

    return renderizar_tablas_secretaria()

def renderizar_tablas_secretaria():
    modelo, modelo_esquema, modelos_esquemas = obtener_modelo(CITAS)
    citas = obtener_filas(modelo, modelos_esquemas)
    modelo, modelo_esquema, modelos_esquemas = obtener_modelo(ENFERMERAS)
    enfermeras = obtener_filas(modelo, modelos_esquemas)
    modelo, modelo_esquema, modelos_esquemas = obtener_modelo(OFERTAS)
    ofertas = obtener_filas(modelo, modelos_esquemas)
    modelo, modelo_esquema, modelos_esquemas = obtener_modelo(PACIENTES)
    pacientes = obtener_filas(modelo, modelos_esquemas)
    print(pacientes)
    modelo, modelo_esquema, modelos_esquemas = obtener_modelo(SECRETARIAS)
    secretarias = obtener_filas(modelo, modelos_esquemas)
    modelo, modelo_esquema, modelos_esquemas = obtener_modelo(SEDES)
    sedes = obtener_filas(modelo, modelos_esquemas)
    modelo, modelo_esquema, modelos_esquemas = obtener_modelo(TELEFONOS)
    telefonos = obtener_filas(modelo, modelos_esquemas)
    return render_template('secretarias.html', 
                            citas=citas, 
                            enfermeras=enfermeras,
                            ofertas=ofertas,
                            pacientes=pacientes,
                            secretarias=secretarias,
                            sedes=sedes,
                            telefonos=telefonos,
                            isLogged=True)

@app.route('/actualizar_paciente', methods=['POST'])
def actualizar_paciente():

    datos = {}
    cedula = request.form['cedula']
    nombre = request.form['nombre']
    apellidos = request.form['apellidos']
    datos["nombre"] = nombre
    datos["apellidos"] = apellidos
    modelo, modelo_esquema, modelos_esquemas = obtener_modelo(PACIENTES)
    actualizar_fila(modelo, modelo_esquema, dict(datos), cedula)

    return renderizar_tablas_secretaria()

@app.route('/borrar_paciente', methods=['POST'])
def borrar_paciente():

    cedula = request.form['cedula']
    modelo, modelo_esquema, modelos_esquemas = obtener_modelo(PACIENTES)
    eliminar_fila(modelo, modelo_esquema, cedula)

    return renderizar_tablas_secretaria()


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