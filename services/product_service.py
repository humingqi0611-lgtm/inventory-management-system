from models import db
from models.product import Product


# 添加商品
def add_product(data):
    product = Product(
        name=data['name'],
        price=data['price'],
        description=data.get('description', '')
    )

    db.session.add(product)
    db.session.commit()

    return product


# 查询所有商品
def get_products():
    return Product.query.all()


# 根据ID查询商品
def get_product(id):
    return db.session.get(Product, id)


# 修改商品
def update_product(product, data):
    product.name = data.get('name', product.name)
    product.price = data.get('price', product.price)
    product.description = data.get(
        'description', product.description
    )

    db.session.commit()


# 删除商品
def delete_product(product):
    db.session.delete(product)
    db.session.commit()