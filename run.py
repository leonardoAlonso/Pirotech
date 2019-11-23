from api import create_app
from api.config import DevelopmentConfig
if __name__ == "__main__":
    app = create_app(DevelopmentConfig)
    app.run(debug=True)