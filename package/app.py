from types import ModuleType
from flask import Flask, Blueprint
from package import config
from package import services

def register_blueprints(app: Flask, routes_module: ModuleType) -> Flask:
    """
    Register blueprints from the routes module to the Flask app passed in
    """
    for blueprint in vars(routes_module).values():
        if isinstance(blueprint, Blueprint):
            app.register_blueprint(blueprint)

def create_app(environment: str) -> Flask:
    """
    Create a flask app
    Return the app after setting config and registering blueprints
    """
    app = Flask('MyApp')
    
    app.config.from_object(
        config.config[environment]
    )
    services.cache.init_app(app)

    from package import routes
    register_blueprints(app, routes)
    return app

if __name__ == '__main__':
    import sys
    environment = sys.argv[1]
    create_app(environment).run()
