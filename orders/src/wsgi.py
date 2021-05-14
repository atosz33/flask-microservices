from app.app import get_app_with_config
from config import ProductionConfig

app, mongodb = get_app_with_config(ProductionConfig)

if __name__ == '__main__':
    app.run()
