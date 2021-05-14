class ProductionConfig:
    MONGO_URI = f"mongodb://mongodb:27017/orders"

class TestConfig:
    MONGO_HOST = 'mongodb'
    MONGO_PORT = 27017
    MONGO_DBNAME = 'orders'
    MONGO_URI = f"mongodb://{MONGO_HOST}:{MONGO_PORT}/{MONGO_DBNAME}"
    TESTING = True
