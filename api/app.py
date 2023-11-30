from flask import Flask
from api.config import Config
from api.customers import customer_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(customer_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
