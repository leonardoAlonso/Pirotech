from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import db

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    
    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    db.init_app(app)

    return app


if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)