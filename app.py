from flask import Flask

from config import Config
from routes.product import product_bp
from routes.stock import stock_bp
from routes.logs import logs_bp
from models import db
from models.product import Product
from models.stock import Stock
from models.stock_log import StockLog

app = Flask(__name__)
# 处理 404：找不到页面
@app.errorhandler(404)
def not_found(error):
    return {
        'error': '请求的资源不存在',
        'code': 404
    }, 404


# 处理 500：服务器内部错误
@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()

    return {
        'error': '服务器内部错误，请稍后重试',
        'code': 500
    }, 500

app.config.from_object(Config)
db.init_app(app)

# 注册蓝图
app.register_blueprint(product_bp)
app.register_blueprint(stock_bp)
app.register_blueprint(logs_bp)
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return '库存管理系统启动成功！'


if __name__ == '__main__':
    app.run(debug=True)