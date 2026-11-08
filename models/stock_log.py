from models import db


class StockLog(db.Model):
    __tablename__ = 'stock_logs'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    product_id = db.Column(
        db.Integer,
        db.ForeignKey('products.id'),
        nullable=False
    )

    action = db.Column(
        db.String(20),
        nullable=False
    )

    quantity = db.Column(
        db.Integer,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=db.func.current_timestamp()
    )