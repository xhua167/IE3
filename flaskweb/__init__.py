from flask import Flask
from pymongo import MongoClient
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_basicauth import BasicAuth

# Initialising the flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = '4d7e72400c6b35d23f38678282d3ba5d'

# Set the password to protect the web
app.config['BASIC_AUTH_USERNAME'] = 'admin'
app.config['BASIC_AUTH_PASSWORD'] = 'help1024'
app.config['BASIC_AUTH_FORCE'] = True
basic_auth = BasicAuth(app)

# Set the MongoDB database
uri = 'mongodb://lenomongo726:cN1mZVS8a0fIOZVm4dvZwGCmpgnWNeah0YSsFZ8DuyTwmpJWC9Z7k05WVvEPSvhk26Lt0QnBlP4P7lxofJ7Rzw==@lenomongo726.documents.azure.com:10255/?ssl=true&replicaSet=globaldb'

client = MongoClient(uri)
db = client.IE

# Set the login manager of the app
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# Import the app routes
from flaskweb import routes

