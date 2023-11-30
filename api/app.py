from flask import Flask, g
from api.db import init_db, close_db, get_db
from api.config import Config
from api.customers import customer_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(customer_bp)

    @app.before_request
    def before_request():
        g.db = get_db()

    @app.teardown_appcontext
    def teardown_appcontext(e=None):
        close_db(e)

    return app


if __name__ == "__main__":
    app = create_app()

    # Initialize the database before running the app
    with app.app_context():
        init_db()

    app.run(debug=True)
