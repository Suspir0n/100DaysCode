import datetime
from app import db, ma
from sqlalchemy.dialects import *

# class product
# Table of products and yours fields.
class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    createAt = db.Column(db.DateTime, default=datetime.datetime.now())
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    amount =db.Column(db.Integer, nullable=False)

    def create(self):
        db.session.add(self)
        db.session.commit()

    def __init__(self, name, description, price, amount):
        self.name = name
        self.description = description
        self.price = price
        self.amount = amount
    
    def __repr__(self):
        return '' % self.id
db.create_all()
# class productSchema
# Schema of Marshmallow for facilitate the use of json
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'createAt', 'name', 'description', 'price', 'amount')

product_schema = ProductSchema()
products_schema = ProductSchema(many = True)