from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow  

def create_app():
    app = Flask(__name__)
    return app

# config databaseS
app_ext = create_app()
app_ext.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost:3306/apisingle'

# init DB 
db = SQLAlchemy(app_ext)
ma = Marshmallow(app_ext)

from .models import product
from .controllers import productController
from .routes import router  