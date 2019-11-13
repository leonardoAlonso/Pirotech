from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from resources.models import db

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api/v1')
    with app.app_context():
        db.init_app(app)
        db.create_all()
    return app


if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)