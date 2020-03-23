from flask_migrate import Migrate
from api import create_app
from api.config import DevelopmentConfig
from api.models import db
from api.Clientes.models import Cliente
from api.Users.models import User

app = create_app(DevelopmentConfig)
migrate = Migrate(app, db)


if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
