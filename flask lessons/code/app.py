from logging import DEBUG
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from user import User, UserRegister
from items import Items, Item
from security import authinticate, indentify

# ---------------------------------------------------- Global -----------------------------------------------------------
app = Flask(__name__)
api = Api(app)
app.secret_key = 'mdcsjcdsi23903030-23-021idmjwq'
jwt = JWT(app, authinticate, indentify) # athinticate app with two methods, authinticate and identity


# ---------------------------------------------- Connect Resources to URL -----------------------------------------------
api.add_resource(Item,'/item/<string:name>')
api.add_resource(Items,'/items')
api.add_resource(UserRegister, '/regester')

app.run(port =8080, debug=True)