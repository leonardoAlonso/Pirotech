from flask_migrate import Migrate
from api import create_app
from api.config import DevelopmentConfig
from api.models import db
from api.Clientes.models import Cliente
from api.Users.models import User

import os

try:
    env = os.environ['APPLICATION_ENV']
except KeyError as e:
    print('Unknown environment key, defaulting to Development')
    env = 'DevelopmentConfig'
print("* App runing on {} environment".format(env))
app = create_app("api.config.%s"%env)
migrate = Migrate(app, db)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
