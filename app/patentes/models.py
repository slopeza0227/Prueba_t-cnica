from app.db import db, BaseModelMixin

class Patente(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Patente({self.name})'

    def __str__(self):
        return f'{self.name}'