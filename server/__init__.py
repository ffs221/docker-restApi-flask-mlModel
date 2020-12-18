"""
Server Module
"""
import sys

from flask import Flask, jsonify
from flask_cors import CORS
from flask_marshmallow import Marshmallow

sys.stdout.flush()
ma = Marshmallow()


def create_app(app_config):
    app = Flask(__name__)
    app.config.from_object(app_config)
    CORS(app)
    ma.init_app(app)
    from .controller import santander_controller
    app.register_blueprint(santander_controller.santander)

    # A simple page that says server status
    @app.route('/')
    def home():
        return jsonify('The server is running!!')

    return app
