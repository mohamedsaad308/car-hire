from flask import Blueprint, request, jsonify, abort
from flask.views import MethodView
from api.db import get_db

customer_bp = Blueprint("customer", __name__, url_prefix="/api/customers")


class CustomerView(MethodView):
    def get(self, customer_id):
        try:
            customer = self.get_customer_from_db(customer_id)

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
                abort(404, description="Customer not found")

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def put(self, customer_id):
        try:
            data = request.json
            self.validate_input(data)

            db = get_db()
            with db.cursor() as cursor:
                self.update_customer(cursor, customer_id, data)
                db.commit()

            return jsonify({"message": "Customer updated successfully"})

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def delete(self, customer_id):
        try:
            db = get_db()
            with db.cursor() as cursor:
                self.delete_customer(cursor, customer_id)
                db.commit()

            return jsonify({"message": "Customer deleted successfully"})

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def get_customer_from_db(self, customer_id):
        db = get_db()
        with db.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM customers WHERE customer_id=%s", (customer_id,)
            )
            return cursor.fetchone()

    def update_customer(self, cursor, customer_id, data):
        cursor.execute("SELECT 1 FROM customers WHERE customer_id=%s", (customer_id,))
        if cursor.fetchone():
            cursor.execute(
                "UPDATE customers SET first_name=%s, last_name=%s, email=%s, phone=%s WHERE customer_id=%s",
                (
                    data["first_name"],
                    data["last_name"],
                    data["email"],
                    data["phone"],
                    customer_id,
                ),
            )
        else:
            abort(404, description="Customer not found")

    def delete_customer(self, cursor, customer_id):
        cursor.execute("SELECT 1 FROM customers WHERE customer_id=%s", (customer_id,))
        if cursor.fetchone():
            cursor.execute("DELETE FROM customers WHERE customer_id=%s", (customer_id,))
        else:
            abort(404, description="Customer not found")

    def validate_input(self, data):
        required_fields = ["first_name", "last_name", "email", "phone"]
        for field in required_fields:
            if field not in data:
                abort(400, description=f"Missing '{field}' in request data")
