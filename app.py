from controllers import user_controller
from database import initialize_database
from flask import Flask
import os
from init import db, ma
from controllers.crag_controller import crag_controller
from controllers.route_controller import route_controller
from controllers.auth_controller import auth_controller
from marshmallow.exceptions import ValidationError


def create_app():
    app = Flask(__name__)

    @app.errorhandler(ValidationError)
    def validation_error(err):
        return {'error': err.messages}, 400
    
    initialize_database(app)

    # Register the blueprints for the controllers
    app.register_blueprint(crag_controller)
    app.register_blueprint(route_controller)
    app.register_blueprint(auth_controller)
    app.register_blueprint(user_controller)

    return app


if __name__ == '__main__':
    app.run(debug=True)
