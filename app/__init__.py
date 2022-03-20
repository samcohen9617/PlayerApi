from flask import Flask

def app_register_blueprints(app: Flask):
    """
    Register all blueprints from here
    :param app: Flask App
    :return: None
    """
    from app.api import balldontlie

    # Register routes
    _blue_prints = [balldontlie.blueprint.BP]
    for _bp in _blue_prints:
        app.register_blueprint(_bp)

def create_app():
    """
    create the app
    """
    app = Flask(__name__)
    app_register_blueprints(app)
    return app
