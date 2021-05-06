from flask import Flask, jsonify, request
from .models import Orders
from .db import mongodb

app = Flask(__name__)


app.config['MONGODB_SETTINGS'] = {
        'db': 'orders',
        'host': '0.0.0.0',
        'port': 27017
}

mongodb.init_app(app)



@app.route('/order', methods=['GET'])
def list_all_order():
    return jsonify(Orders.objects())

@app.route('/order/<int:num>', methods=['GET'])
def show_specific_order(num):
    order = Orders.objects.get(num)
    return jsonify(order)

@app.route('/order/<int:num>', methods=['PUT'])
def modify_order(num):
    json_data = request.get_json()
    print("tess")

@app.route('/order', methods=['POST'])
def add_order():
    json_data = request.get_json()
    order = Orders(**json_data)
    order.save()
    return jsonify(json_data), 200
    

@app.route('/order/<int:num>', methods=['DELETE'])
def remove_order(num):
    return jsonify({'element_removed': num}), 200
