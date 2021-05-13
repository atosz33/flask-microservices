from flask import Flask, jsonify, request
import json
from .models import Orders
from .db import mongodb


def get_app_with_config(config):
    app = Flask(__name__)
    app.config.from_object(config)
    mongodb.init_app(app)

    @app.route('/')
    def index():
        return jsonify({"result": "success"}), 200

    @app.route('/order', methods=['GET'])
    def list_all_order():
        return jsonify(Orders.objects())

    @app.route('/order/<int:num>', methods=['GET'])
    def show_specific_order(product_id):
        order = Orders.objects.get(product_id=product_id)
        return jsonify(order)

    @app.route('/order/<int:num>', methods=['PUT'])
    def modify_order(num):
        json_data = request.get_json()
        print("tess")

    @app.route('/order', methods=['POST'])
    def add_order():
        try:
            json_data = request.get_json(force=True)
        except:
            return throw_error(400, 'Invalid JSON message recieved')

        order = Orders(**json_data)
        order.save()

        return jsonify(json_data), 201

    @app.route('/order/<int:num>', methods=['DELETE'])
    def remove_order(num):
        return jsonify({'element_removed': num}), 200

    def throw_error(error_code, error_message):
        return jsonify({'error_code':error_code, 'message':error_message}), error_code

    def is_json_valid(data):
        try:
            json.loads(data)
            return True
        except ValueError:
            return False

    return app, mongodb
