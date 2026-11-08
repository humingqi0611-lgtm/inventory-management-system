from models import db
from models.product import Product
from models.stock import Stock
from models.stock_log import StockLog


# 商品入库
def stock_in(product_id, quantity):
    product = db.session.get(Product, product_id)

    if not product:
        return False, '商品不存在'

    if quantity <= 0:
        return False, '入库数量必须大于0'

    stock = Stock.query.filter_by(
        product_id=product_id
    ).first()

    if not stock:
        stock = Stock(product_id=product_id, quantity=0)
        db.session.add(stock)

    stock.quantity += quantity

    log = StockLog(
        product_id=product_id,
        action='入库',
        quantity=quantity
    )

    db.session.add(log)
    db.session.commit()

    return True, '入库成功！'


# 商品出库
def stock_out(product_id, quantity):
    if quantity <= 0:
        return False, '出库数量必须大于0'

    stock = Stock.query.filter_by(
        product_id=product_id
    ).first()

    if not stock or stock.quantity < quantity:
        return False, '库存不足'

    stock.quantity -= quantity

    log = StockLog(
        product_id=product_id,
        action='出库',
        quantity=quantity
    )

    db.session.add(log)
    db.session.commit()

    return True, '出库成功！'