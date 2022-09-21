from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import config

#endpoints
from routes import Joke, Mathematical

app=Flask(__name__)
app.config['SQLALCHEMY_BINDS'] = {}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

CORS(app, resources={'*':{'origins': 'http://localhost:9300'}})


def page_not_found(error):
    return '<h1>End Point not found</h1>',404

if __name__ == '__main__':
    app.config.from_object(config['development'])

    #planos de rutas
    app.register_blueprint(Joke.app, url_prefix='/api/jokes/')
    app.register_blueprint(Mathematical.app, url_prefix='/api/mathematical/')
    app.register_error_handler(404,page_not_found)
    app.run()
