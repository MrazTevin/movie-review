from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config_name):
    # Initializing application
    app = Flask(__name__)

    #creating the app configurations
    app.config.from_object(config_options[config_name])

    #registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #initializing Flask Extensions
    bootstrap.init_app(app)

    #setting config
    from .request import configure_request
    configure_request(app)

    #will add the views and forms
    return app
