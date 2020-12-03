# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
import datetime

# init app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost:3306/apisingle'

# init DB
db = SQLAlchemy(app)
ma = Marshmallow(app)

from .models import product
from .controllers import productController
from .routes import router