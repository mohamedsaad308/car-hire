from flask import Blueprint, request, jsonify
from flask.views import MethodView
from api.db import get_db

customer_bp = Blueprint("customer", __name__, url_prefix="/api/customers")


class CustomerView(MethodView):
    def get(self, customer_id):
        try:
            db = get_db()
            cursor = db.cursor()

            cursor.execute(
                "SELECT * FROM customers WHERE customer_id=%s", (customer_id,)
            )
            customer = cursor.fetchone()

            if customer:
                customer_data = {
                    "customer_id": customer[0],
                    "first_name": customer[1],
                    "last_name": customer[2],
                    "email": customer[3],
                    "phone": customer[4],
                }
                return jsonify(customer_data)
            else:
                return jsonify({"message": "Customer not found"}), 404

        except Exception as e:
            return jsonify({"error": str(e)}), 500

        finally:
            cursor.close()
