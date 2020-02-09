from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from api import create_app
from api.config import DevelopmentConfig
from api.models import db
from api.Clientes.models import Cliente
from api.Users.models import User

app = create_app(DevelopmentConfig)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == "__main__":
    manager.run()