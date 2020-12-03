from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# init app
app = Flask(__name__)
app.config.from_object('config')

# init DB
db = SQLAlchemy(app)

# init Marshmallow
ma = Marshmallow(app)

from .models import product
from .controllers import productController
from .routes import router