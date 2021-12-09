from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from db import db

from security import authenticate, identify
from resources.user import UserRegister
from resources.item import Item, ItemsList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.secret_key = "kate"
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identify)


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemsList, '/items')
api.add_resource(UserRegister, '/Register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

db.init_app(app)
app.run(port=5000, debug=True)
