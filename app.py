from flask import Flask
from config import MONGO_ROUTE, SECRET_KEY
from flask_pymongo import PyMongo

app = Flask(__name__)



#DB
app.config['SECRET_KEY'] = SECRET_KEY
app.config['MONGO_URI'] = MONGO_ROUTE
mongo = PyMongo(app)



# Routes 
from routes.home import home
app.register_blueprint(home)
