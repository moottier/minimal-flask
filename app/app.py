from types import ModuleType
from flask import Flask, Blueprint

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

    from app.config import config
    app.config.from_object(
        config[environment]
    )

    from app.models import db, migrate
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)

    from app.services import cache
    cache.init_app(app)

    from app import routes
    register_blueprints(app, routes)

    return app

if __name__ == '__main__':
    import sys
    environment = sys.argv[1]
    create_app(environment).run()
