# customer/urls.py
from api.customers.views import CustomerView, customer_bp

customer_bp.add_url_rule(
    "/<int:customer_id>", view_func=CustomerView.as_view("customers"),
)
