from flask import Flask
from flask_restplus import Api

from instance.config import app_config


def create_app(config_name):
    # Create flask app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.url_map.strict_slashes = False

    # Enable swagger editor
    app.config['SWAGGER_UI_JSONEDITOR'] = True

    api = Api(app=app,
              title="Foodie",
              version='1.0',
              doc='/api/v1/doc',
              description='Foodie is a food delivery service app for a restaurant'
              )

    from resources.orders import api as orders
    api.add_namespace(orders, path='/api/v1')
    return app
