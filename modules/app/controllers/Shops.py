'''controller and routes for the shops'''

import os
from flask import request, jsonify
from flask_jwt_extended import (create_access_token, create_refresh_token,
jwt_required, jwt_refresh_token_required, get_jwt_identity)
from app import app, mongo, flask_bcrypt, jwt
from app.schemas import validate_shop
import logger

ROOT_PATH = os.environ.get('ROOT_PATH')
