from models.stock_log import StockLog


# 查询所有库存变动记录
def get_logs():
    logs = StockLog.query.order_by(
        StockLog.created_at.desc()
    ).all()

    return logs