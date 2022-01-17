from .. import db, app
from flask import render_template, request, jsonify
from ..models import Citas, Cuentas, Enfermeras, Ofertas, Pacientes, Secretarias, Sedes, Telefonos

# user_schema = User.UserSchema()
# users_schema = User.UserSchema(many=True)

# @app.route('/')
# def home_page():
#     allUsers = User.User.query.all()
#     result = users_schema.dump(allUsers)
#     return render_template('home.html', data=result)

# @app.route('/users', methods=['POST'])
# def create_user():

#     name = request.json['name']
#     age = request.json['age']

#     newUser = User.User(name, age)
#     db.session.add(newUser)
#     db.session.commit()

#     return user_schema.jsonify(newUser)

# @app.route('/users', methods=['GET'])
# def get_users():
#     allUsers = User.User.query.all()
#     result = users_schema.dump(allUsers)
#     return jsonify(result)

# @app.route('/users/<id>', methods=['GET'])
# def get_user(id):
#     user = User.User.query.get(id)
#     return user_schema.jsonify(user)

# @app.route('/users/<id>', methods=['PUT'])
# def update_user(id):

#     user = User.User.query.get(id)
#     name = request.json['name']
#     age = request.json['age']

#     user.name = name
#     user.age = age

#     db.session.commit()

#     return user_schema.jsonify(user)

# @app.route('/users/<id>', methods=['DELETE'])
# def delete_user(id):
#     user = User.User.query.get(id)
#     db.session.delete(user)
#     db.session.commit()
    
#     return user_schema.jsonify(user)

db.create_all()