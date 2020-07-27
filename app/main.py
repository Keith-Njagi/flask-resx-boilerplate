import os

from flask import Flask, Blueprint
from flask_cors import CORS

from configurations import *
from resources import  blueprint , jwt # , mail,
from models import db, ma

app = Flask(__name__)



app.config.from_object(Development)

CORS(app)
app.register_blueprint(blueprint)
# mail.init_app(app)
jwt.init_app(app)
db.init_app(app)
ma.init_app(app)


basedir = os.path.abspath(os.path.dirname(__file__))

@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3100)