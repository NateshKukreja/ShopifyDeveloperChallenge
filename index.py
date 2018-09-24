from flask import *
import json
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

@app.route('/')
def home_page():
    return "hi"

@auth.get_password
def get_password(username):
    if username == "Natesh":
        return "isGreat"
    return None

@auth.error_handler
def unauthorized():
    return json.dumps({"error": 401, "description":"Unauthorized access"}, indent=2), 401

@app.route('/api/v1.0/products', methods=['GET'])
@auth.login_required
def get_products():
    return json.dumps(data["products"], indent=2), 200

@app.route('/api/v1.0/products', methods=['POST'])
def create_product():
    if not request.json or not "name" in request.json:
        return json.dumps({"error":"Missing name or data not in json format"}, indent = 2), 400

    product = {
        "product_id":data["products"][-1]["product_id"]+1,
        "shop_id": 1,
        "line_id": 30,
        "name": request.json.get("name", "")
    }
    data["products"].append(product)
    data["shops"][0]["products"].append(product)

    data["lines"].append({"line_id":product["line_id"],"product_id":product["product_id"], "total":5, "quantity": 5})
    
    return json.dumps(data["products"], indent=2), 200 
    
@app.route('/api/v1.0/line', methods=['GET'])
@auth.login_required
def get_line():
    return json.dumps(data["line"], indent=2), 200

@app.route('/api/v1.0/orders', methods=['GET'])
@auth.login_required
def get_orders():
    return json.dumps(data["orders"], indent=2), 200

@app.route('/api/v1.0/orders', methods=['POST'])
def create_order():
    if not request.json or not "lines" in request.json:
        return json.dumps({"error":"Missing line items in json format"}, indent = 2), 400
    
    lines = request.json.get("lines","")
    
    data["lines"].append(lines)
    order_id = data["orders"][-1]["order_id"]+1
    price = 0
    for line in lines:
        price = price + line["price"]
    
    data["orders"].append({"order_id":order_id, "lines":lines, "price":price})

    return json.dumps(data["orders"], indent=2), 200 

    
@app.route('/api/v1.0/shops', methods=['GET'])
@auth.login_required
def get_shops():
    return json.dumps(data["shops"], indent=2), 200

@app.route('/api/v1.0/shops', methods=['POST'])
def create_shop():
    if not request.json or not "shop" in request.json:
        return json.dumps({"error":"Missing name in json format"}, indent = 2), 400
    shop = request.json.get("shop","")
    data["shops"].append({"shop_id":data["shops"][-1]["shop_id"]+1, "name":shop["name"],"products":[], "orders":[]})
    
    return json.dumps(data["shops"], indent=2), 200
@app.route('/api/v1.0/shops/<int:shop_id>', methods=['GET'])
@auth.login_required
def get_shop(shop_id):
    shop = [shop for shop in data["shops"] if shop["shop_id"] == shop_id]
    if len(shop) == 0:
        return json.dumps({"error":404, "description": "Shop not found"}, indent=2), 404
    return json.dumps({"shop": shop}, indent = 2), 200

@app.route('/api/v1.0/shops/<int:shop_id>', methods=['DELETE'])
@auth.login_required
def delete_shop(shop_id):

    flag = False
    for i in range(len(data["shops"])):
        if data["shops"][i]["shop_id"] == shop_id:
            flag = True
            del data["shops"][i]
    
    if not flag:
        return json.dumps({"error":404, "description": "Shop not found"}, indent=2), 404

    return json.dumps({"shops":data["shops"]}, indent=2), 200
    
@app.route('/api/v1.0/products/<int:product_id>', methods=['GET'])
@auth.login_required
def get_product(product_id):
    product = [product for product in data["products"] if product["product_id"] == product_id]
    if len(product) == 0:
        return json.dumps({"error":404, "description": "Product not found"}, indent=2), 404
    return json.dumps({"product": product}, indent = 2), 200

@app.route('/api/v1.0/orders/<int:order_id>', methods=['GET'])
@auth.login_required
def get_order(order_id):
    order = [order for order in data["orders"] if order["order_id"] == order_id]
    if len(order) == 0:
        return json.dumps({"error":404, "description": "Order not found"}, indent=2), 404
    return json.dumps({"order": order}, indent = 2), 200

@app.route('/api/v1.0/line/<int:line_id>', methods=['GET'])
@auth.login_required
def get_line_id(line_id):
    line = [line for line in lines if data["lines"] == line_id]
    if len(line) == 0:
        return json.dumps({"error":404, "description": "Line not found"}, indent=2), 404
    return json.dumps({"line": line}, indent = 2), 200



if __name__ == "__main__":
    app.run(debug=True)
    
data = {
    "shops":[
        {
            "shop_id":1,
            "name":"Loblaws",
            "products": [
                {
                    "product_id":10,
                    "name":"Milk",
                    "line_id":30,                        "shop_id":1
                },
                {
                    "product_id":11,
                    "name":"Eggs",
                    "line_id":31,
                    "shop_id":1
                }
            ],
            "orders":[
                {
                    "order_id":20,
                    "total": 5
                }
            ]
        }
    ],
    "products": [
        {
            "product_id":10,
            "name":"Milk",
            "line_id":30,
            "shop_id":1
        },
        {
            "product_id":11,
            "name":"Eggs",
            "line_id":31,
            "shop_id":1
        },
        {
            "product_id":12,
            "name":"Bread",
            "line_id":32,
            "shop_id":1
        },
    ],
    "orders": [
        {
            "order_id": 20,
            "lines": [
                {
                    "line_id": 30,
                    "product_id": 10,
                    "quantity": 1,
                    "price": 5
                }
            ],
            "total": 5
        }
    ],
    "lines":[
        {
            "line_id": 30,
            "product_id": 10,
            "quantity": 1,
            "price": 5
        }
    ]
}