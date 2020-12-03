from app import db
from flask import request, jsonify
from ..models.product import Product, product_schema, products_schema

def get_products():
    name = request.args.get('name')
    if name:
        products = Product.query.filter(Product.name.like(f'%{name}')).all()
    else:
        products = Product.query.all()
    if products:
        result = products_schema.dump(products)
        return  jsonify({'message': 'successfully fetched', 'data': result})
    
    return jsonify({'message': 'nothing found', 'data': {}})

def get_product(uid):
    product = Product.query.get(uid)
    if product:
        result = product_schema.dump(product)
        return jsonify({'message': 'successfully fetched', 'data': result}), 201

    return jsonify({'message': 'this product no exist', 'data': {}}), 404

