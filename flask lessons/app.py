from flask import Flask, jsonify, request

app = Flask(__name__)

orders = [
    {
        'number': 1,
        'price': 1.0,
        'items': []
    },
    {
        'number': 2,
        'price': 5.00,
        'items': []
    }
]

@app.get('/')
def get_home():
    return 'Welcome'

# Get orders list
@app.get('/orders')
def get_orders():
    return jsonify({'orders': orders})
# get one order by number
@app.get('/orders/<int:number>')
def get_one_order(number):
    for order in orders:
        if order['number'] == number:
            return jsonify(order)
    return jsonify({'message': 'Order does not exist'})

# add one order
app.post('/orders')
def create_order():
    request_data = request.get_json()
    new_order = {
        'number': request_data['number'],
        'price': request_data['price'],
        'items': request_data['items']
    }
    orders.append(new_order)
    return jsonify(new_order)

# add list of items to order
app.post('orders/<int:order_number>')
def create_items(order_number):
    request_data = request.get_json()
    for order in orders:
        if order['number'] == order_number:
            create_items = request_data['items']
            return jsonify(create_items)
    return jsonify({'Message': 'Something went wrong'})
# get one item details
# @app.get('/orders/<int:order_number>/')


app.run(port= 3000)