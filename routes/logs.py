from flask import Blueprint, jsonify
from services.logs_service import get_logs
from models.product import Product
from models import db

logs_bp = Blueprint('logs', __name__, url_prefix='/logs')


# 查询库存变动记录
@logs_bp.route('/', methods=['GET'])
def list_logs():
    logs = get_logs()

    result = []

    for log in logs:
        product = db.session.get(Product, log.product_id)

        result.append({
            'id': log.id,
            'product_id': log.product_id,
            'product_name': product.name if product else '未知商品',
            'action': log.action,
            'quantity': log.quantity,
            'created_at': log.created_at.strftime('%Y-%m-%d %H:%M:%S')
        })

    return jsonify(result)