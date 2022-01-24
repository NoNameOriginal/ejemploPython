from .. import db, app
from flask import render_template, request, jsonify

def crear_fila(Modelo, ModeloSchema, DictParam):

    crear_fila = Modelo(DictParam)
    db.session.add(crear_fila)
    db.session.commit()

    return ModeloSchema.jsonify(crear_fila)

def obtener_filas(Modelo, ModeloSchema):
    todas_las_filas = Modelo.query.all()
    result = ModeloSchema.dump(todas_las_filas)
    return result

def obtener_fila(Modelo, ModeloSchema, id):
    fila = Modelo.query.get(id)
    return fila

def actualizar_fila(Modelo, ModeloSchema, DictParam,id):
    fila = Modelo.query.get(id)
    for key, value in DictParam.items():
        setattr(fila, key, value)

    db.session.commit()

    return ModeloSchema.jsonify(fila)

def eliminar_fila(Modelo, ModeloSchema, id):
    fila = Modelo.query.get(id)
    db.session.delete(fila)
    db.session.commit()
    
    return ModeloSchema.jsonify(fila)