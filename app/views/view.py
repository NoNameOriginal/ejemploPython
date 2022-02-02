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

def renderizar_tablas_clientes():
    modelo, modelo_esquema, modelos_esquemas = obtener_modelo(CITAS)
    citas = obtener_filas(modelo, modelos_esquemas)
    return render_template('clientes.html', 
                            citas=citas)
    
@app.route('/actualizar_cita', methods=['POST'])
def actualizar_cita():

    datos = {}
    id = request.form['id']
    fecha = request.form['fecha']
    hora = request.form['hora']
    zona = request.form['zona']
    duracion = request.form['duracion']
    print(fecha)
    datos["fecha"] = fecha
    datos["hora"] = hora
    datos["zona"] = zona
    datos["duracion"] = duracion
    modelo, modelo_esquema, modelos_esquemas = obtener_modelo(CITAS)
    actualizar_fila(modelo, modelo_esquema, dict(datos), id)

    return renderizar_tablas_clientes()

@app.route('/actualizar_cita_secretaria', methods=['POST'])
def actualizar_cita_secretaria():

    datos = {}
    id = request.form['id']
    fecha = request.form['fecha']
    hora = request.form['hora']
    zona = request.form['zona']
    duracion = request.form['duracion']
    datos["fecha"] = fecha
    datos["hora"] = hora
    datos["zona"] = zona
    datos["duracion"] = duracion
    modelo, modelo_esquema, modelos_esquemas = obtener_modelo(CITAS)
    actualizar_fila(modelo, modelo_esquema, dict(datos), id)

    return renderizar_tablas_secretaria()

@app.route('/actualizar_enfermera', methods=['POST'])
def actualizar_enfermera():

    datos = {}
    tarjetaProfesional = request.form['tarjetaProfesional']
    cedula = request.form['cedula']
    nombre = request.form['nombre']
    sede_id = request.form['sede_id']
    datos["tarjetaProfesional"] = tarjetaProfesional
    datos["nombre"] = nombre
    datos["sede_id"] = sede_id
    modelo, modelo_esquema, modelos_esquemas = obtener_modelo(ENFERMERAS)
    actualizar_fila(modelo, modelo_esquema, dict(datos), tarjetaProfesional)

    return renderizar_tablas_secretaria()

@app.route('/actualizar_oferta', methods=['POST'])
def actualizar_oferta():

    datos = {}
    id = request.form['id']
    precio = request.form['precio']
    zona = request.form['zona']
    inicio = request.form['inicio']
    fin = request.form['fin']
    datos["precio"] = precio
    datos["zona"] = zona
    datos["inicio"] = inicio
    datos["fin"] = fin
    modelo, modelo_esquema, modelos_esquemas = obtener_modelo(OFERTAS)
    actualizar_fila(modelo, modelo_esquema, dict(datos), id)

    return renderizar_tablas_secretaria()

@app.route('/actualizar_paciente', methods=['POST'])
def actualizar_paciente():

    datos = {}
    cedula = request.form['cedula']
    nombre = request.form['nombre']
    apellidos = request.form['apellidos']
    sede_id = request.form['sede_id']
    datos["nombre"] = nombre
    datos["apellidos"] = apellidos
    datos["sede_id"] = sede_id
    modelo, modelo_esquema, modelos_esquemas = obtener_modelo(PACIENTES)
    actualizar_fila(modelo, modelo_esquema, dict(datos), cedula)

    return renderizar_tablas_secretaria()

@app.route('/actualizar_secretaria', methods=['POST'])
def actualizar_secretaria():

    datos = {}
    cedula = request.form['cedula']
    nombre = request.form['nombre']
    sede_id = request.form['sede_id']
    datos["nombre"] = nombre
    datos["sede_id"] = sede_id
    modelo, modelo_esquema, modelos_esquemas = obtener_modelo(SECRETARIAS)
    actualizar_fila(modelo, modelo_esquema, dict(datos), cedula)

    return renderizar_tablas_secretaria()

@app.route('/actualizar_sede', methods=['POST'])
def actualizar_sede():

    datos = {}
    id = request.form['id']
    centroComercial = request.form['centroComercial']
    local = request.form['local']
    horarioApertura = request.form['horarioApertura']
    horarioCierre = request.form['horarioCierre']
    datos["centroComercial"] = centroComercial
    datos["local"] = local
    datos["horarioApertura"] = horarioApertura
    datos["horarioCierre"] = horarioCierre
    modelo, modelo_esquema, modelos_esquemas = obtener_modelo(SEDES)
    actualizar_fila(modelo, modelo_esquema, dict(datos), id)

    return renderizar_tablas_secretaria()

@app.route('/actualizar_telefono', methods=['POST'])
def actualizar_telefono():

    datos = {}
    telefono = request.form['telefono']
    sede_id = request.form['sede_id']
    datos["telefono"] = telefono
    datos["sede_id"] = sede_id
    modelo, modelo_esquema, modelos_esquemas = obtener_modelo(TELEFONOS)
    actualizar_fila(modelo, modelo_esquema, dict(datos), id)

    return renderizar_tablas_secretaria()

@app.route('/borrar_cita', methods=['POST'])
def borrar_cita():

    id = request.form['id']
    modelo, modelo_esquema, modelos_esquemas = obtener_modelo(CITAS)
    eliminar_fila(modelo, modelo_esquema, id)

    return renderizar_tablas_secretaria()

@app.route('/borrar_enfermera', methods=['POST'])
def borrar_enfermera():

    cedula = request.form['cedula']
    modelo, modelo_esquema, modelos_esquemas = obtener_modelo(ENFERMERAS)
    eliminar_fila(modelo, modelo_esquema, cedula)

    return renderizar_tablas_secretaria()

@app.route('/borrar_oferta', methods=['POST'])
def borrar_oferta():

    id = request.form['id']
    modelo, modelo_esquema, modelos_esquemas = obtener_modelo(OFERTAS)
    eliminar_fila(modelo, modelo_esquema, id)

    return renderizar_tablas_secretaria()

@app.route('/borrar_paciente', methods=['POST'])
def borrar_paciente():

    cedula = request.form['cedula']
    modelo, modelo_esquema, modelos_esquemas = obtener_modelo(PACIENTES)
    eliminar_fila(modelo, modelo_esquema, cedula)

    return renderizar_tablas_secretaria()

@app.route('/borrar_secretaria', methods=['POST'])
def borrar_scretaria():

    cedula = request.form['cedula']
    modelo, modelo_esquema, modelos_esquemas = obtener_modelo(SECRETARIAS)
    eliminar_fila(modelo, modelo_esquema, cedula)

    return renderizar_tablas_secretaria()

@app.route('/borrar_sede', methods=['POST'])
def borrar_sede():

    id = request.form['id']
    modelo, modelo_esquema, modelos_esquemas = obtener_modelo(SEDES)
    eliminar_fila(modelo, modelo_esquema, id)

    return renderizar_tablas_secretaria()

@app.route('/borrar_telefono', methods=['POST'])
def borrar_telefono():

    id = request.form['id']
    modelo, modelo_esquema, modelos_esquemas = obtener_modelo(TELEFONOS)
    eliminar_fila(modelo, modelo_esquema, id)

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