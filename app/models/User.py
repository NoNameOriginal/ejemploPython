from .. import db, ma

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70))
    age = db.Column(db.Integer)
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'age')