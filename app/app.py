from types import ModuleType
from flask import Flask, Blueprint
from app import config
from app import routes

def register_blueprints(app: Flask, routes_module: ModuleType) -> Flask:
    """
    Register blueprints from the routes module to the Flask app passed in
    """
    for blueprint in vars(routes_module).values():
        if isinstance(blueprint, Blueprint):
            app.register_blueprint(blueprint)

def create_app(name: str, environment: str) -> Flask:
    """
    Create a flask app
    Return the app after setting config and registering blueprints
    """
    app = Flask(name)
    app.config.from_object(
        get_config(environment)
    )
    register_blueprints(app, routes)
    return app

def get_config(environment: str) -> config.BaseConfig:
    """
    Get a config object for an environment name
    """
    if environment == 'PRD':
        return config.ProductionConfig
    elif environment == 'TEST':
        return config.TestingConfig
    else:
        raise NotImplementedError
