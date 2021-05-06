from flask import Flask, jsonify, request

app = Flask(__name__)

orders = [
        {'name':'titkos'}, {'name':'titkosabb'}
        ]

@app.route('/order', methods=['GET'])
def list_all_order():
    return jsonify(orders)

@app.route('/order/<int:num>', methods=['GET'])
def show_specific_order(num):
    return jsonify(orders[num-1])

@app.route('/order/<int:num>', methods=['PUT'])
def modify_order(num):
    json_data = request.get_json()
    print("tess")
    orders[num]['name'] = json_data['name']
    return jsonify(orders[num])

@app.route('/order', methods=['POST'])
def add_order():
    json_data = requests.get_json()
    number_of_orders = len(orders)+1
    orders.append({number_of_orders:json_data})
    return orders[number_of_orders]

@app.route('/order/<int:num>', methods=['DELETE'])
def remove_order(num):
    if len(orders) > num:
        del orders[num]
    else:
        return jsonify({'not_valid_element': num}), 400
    return jsonify({'element_removed': num}), 200
