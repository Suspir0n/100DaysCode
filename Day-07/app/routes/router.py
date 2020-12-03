from app import app
from flask import jsonify
from ..controllers import productController

@app.route('/', methods = ['GET'])
def get_products():
    return productController.get_products()

@app.route('/products/<uid>', methods = ['GET'])
def get_product(uid):
    return productController.get_product(uid)