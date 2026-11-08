from flask import Blueprint, jsonify, request
from models import db
from models.product import Product
from models.stock import Stock
from services.stock_service import stock_in, stock_out

stock_bp = Blueprint('stock', __name__, url_prefix='/stock')


# 查询库存
@stock_bp.route('/', methods=['GET'])
def get_stock():
    stocks = Stock.query.all()

    result = []

    for s in stocks:
        product = db.session.get(Product, s.product_id)

        result.append({
            'product_id': s.product_id,
            'product_name': product.name if product else '未知商品',
            'quantity': s.quantity
        })

    return jsonify(result)


# 商品入库
@stock_bp.route('/in', methods=['POST'])
def add_stock():
    data = request.get_json()

    success, message = stock_in(
        data['product_id'],
        data['quantity']
    )

    if not success:
        return jsonify({'message': message}), 400

    return jsonify({'message': message})


# 商品出库
@stock_bp.route('/out', methods=['POST'])
def remove_stock():
    data = request.get_json()

    success, message = stock_out(
        data['product_id'],
        data['quantity']
    )

    if not success:
        return jsonify({'message': message}), 400

    return jsonify({'message': message})