from flask import Blueprint, jsonify, request
from services.product_service import (
    add_product,
    get_products,
    get_product,
    update_product,
    delete_product
)

product_bp = Blueprint('product', __name__, url_prefix='/products')


# 添加商品
@product_bp.route('/', methods=['POST'])
def create_product():
    data = request.get_json()
    product = add_product(data)

    return jsonify({
        'message': '商品添加成功！',
        'id': product.id
    }), 201


# 查询商品
@product_bp.route('/', methods=['GET'])
def list_products():
    products = get_products()

    result = []
    for p in products:
        result.append({
            'id': p.id,
            'name': p.name,
            'price': p.price,
            'description': p.description
        })

    return jsonify(result)


# 修改商品
@product_bp.route('/<int:id>', methods=['PUT'])
def edit_product(id):
    product = get_product(id)

    if not product:
        return jsonify({'message': '商品不存在'}), 404

    data = request.get_json()
    update_product(product, data)

    return jsonify({'message': '商品修改成功！'})


# 删除商品
@product_bp.route('/<int:id>', methods=['DELETE'])
def remove_product(id):
    product = get_product(id)

    if not product:
        return jsonify({'message': '商品不存在'}), 404

    delete_product(product)

    return jsonify({'message': '商品删除成功！'})