from flask import *
import pymongo
import json
from app.schemas import validate_shop

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("src/templates/home.html")

@app.route('/api/v1.0', methods=['GET'])
def dummy_endpoint():
    return json.dumps({'data': 'Server running'}), 200

if __name__ == "__main__":
    app.run(debug=True)