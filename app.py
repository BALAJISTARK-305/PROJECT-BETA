from flask import Flask, render_template
from flask_restful import Api
from flask_jwt import JWT
# from flask_sqlalchemy import SQLAlchemy

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList, UploadCSV, Multiple_items
from resources.store import Store, StoreList
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'stark'
api = Api(app)
db.init_app(app)
# db.create_all()


@app.route('/')
def index():
    # Set The upload HTML template '\templates\index.html'
    return render_template('index.html')


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(UploadCSV, '/upload')
api.add_resource(Multiple_items, '/multi')

# if __name__ == '__main__':
#     from db import db
#     db.init_app(app)
