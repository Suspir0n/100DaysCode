from app import app
from flask import jsonify
from ..controllers import productController

@app.route('/products', methods = ['GET'])
def get_products_all():
    return productController.get_products_all()

@app.route('/products/<id>', methods = ['GET'])
def get_product_by_id(id):
    return productController.get_product_by_id(id)

@app.route('/products/<id>', methods = ['PUT'])
def put_product_by_id(id):
    return productController.put_product_by_id(id)

@app.route('/products/<id>', methods = ['DELETE'])
def delete_product_by_id(id):
    return productController.delete_product_by_id(id)

@app.route('/products', methods = ['POST'])
def post_product():
    return productController.post_product()