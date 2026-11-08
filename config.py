class Config:

    # 数据库连接地址
    SQLALCHEMY_DATABASE_URI = 'sqlite:///inventory.db'

    # 是否追踪数据库修改
    SQLALCHEMY_TRACK_MODIFICATIONS = False