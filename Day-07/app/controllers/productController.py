from app import db
from flask import request, jsonify
from ..models.product import Product, product_schema, products_schema

def get_products_all():
    products = Product.query.all()
    if products:
        result = products_schema.dump(products)
        return jsonify({'message': 'successfully fetched', 'data': result}), 201
    return jsonify({'message': 'products no exist', 'data': {}}), 404
    
def get_product_by_id(id):
    product = Product.query.get(id)
    if product:
        result = product_schema.dump(product)
        return jsonify({'message': 'successfully fetched', 'data': result}), 201
    return jsonify({'message': 'product no exist', 'data': {}}), 404

def put_product_by_id(id):
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    amount = request.json['amount']
    product = Product.query.get(id)

    if not product:
        return jsonify({'message': "product don't exist", 'data': {}}), 404

    if product:
        try:
            product.name = name
            product.description = description
            product.price = price
            product.amount = amount
            db.session.commit()
            result = product_schema.dump(product)
            return jsonify({'message': 'successfully updated', 'data': result}), 201
        except:
            return jsonify({'message': 'unable to update', 'data':{}}), 500

def delete_product_by_id(id):
    product = Product.query.get(id)
    if not product:
        return jsonify({'message': "product don't exist", 'data': {}}), 404

    if product:
        try:
            db.session.delete(product)
            db.session.commit()
            result = product_schema.dump(product)
            return jsonify({'message': 'successfully deleted', 'data': result}), 200
        except:
            return jsonify({'message': 'unable to delete', 'data': {}}), 500

def post_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    amount = request.json['amount']
    product = Product(name, description, price, amount)

    try:
        db.session.add(product)
        db.session.commit()
        result = product_schema.dump(product)
        return jsonify({'message': 'successfully registered', 'data': result}), 201
    except:
        return jsonify({'message': 'unable to create', 'data': {}}), 500
