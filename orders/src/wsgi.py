from app.app import get_app_with_config
from config import ProductionConfig

if __name__ == '__main__':
    app, _ = get_app_with_config(ProductionConfig)

    app.run()
