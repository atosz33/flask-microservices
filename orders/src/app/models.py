from .db import mongodb
import datetime

class Orders(mongodb.Document):
    __tablename__ = "orders"

    product_name = mongodb.StringField()
    user_id = mongodb.IntField()
    price = mongodb.IntField()
    shipping_address = mongodb.StringField()
    order_date = mongodb.DateTimeField(default=datetime.datetime.now)
    quantity = mongodb.IntField()
    shipped = mongodb.BooleanField()
    arrived = mongodb.BooleanField()
