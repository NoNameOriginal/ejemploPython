from .. import db, app
from flask import render_template, request, jsonify
from ..models import Citas, Cuentas, Enfermeras, Ofertas, Pacientes, Secretarias, Sedes, Telefonos
from .ManejadorDeBaseDeDatos import *

CITAS="CITAS"
CUENTAS="CUENTAS"
ENFEREMERAS="ENFEREMERAS"
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
    
    return modelo, modelo_esquema, modelos_esquema

# @app.route('/')
# def home_page():
#     allUsers = User.User.query.all()
#     result = users_schema.dump(allUsers)
#     return render_template('home.html', data=result)

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