from models import db


class Stock(db.Model):
    __tablename__ = 'stock'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    product_id = db.Column(
        db.Integer,
        db.ForeignKey('products.id'),
        unique=True,
        nullable=False
    )

    quantity = db.Column(
        db.Integer,
        default=0
    )