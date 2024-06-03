from flask import Flask

def create_app():
    app = Flask(__name__)
    # from . import app as app_module
    app.register_blueprint(app_module.bp)
    return app
