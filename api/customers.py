from flask import Blueprint, jsonify


customer_bp = Blueprint("customers", __name__, url_prefix="/api")


@customer_bp.route("/hello")
def hello_world():
    return jsonify({"message": "Hello World"}), 200
