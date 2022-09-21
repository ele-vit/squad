from app import db, app
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)

class Joke(db.Model):
    __tablename__ = 'jokes'
    id = db.Column(db.String(), primary_key=True)
    joke = db.Column(db.String())
    def __init__(self, id, joke=None):
        self.id = id
        self.joke = joke

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def to_JSON(self):
        return{
                'id':self.id,
                'joke':self.joke,
                'origin':'localhost',
        }


db.create_all()

class JokeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'joke')
