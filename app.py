from flask import Flask
from controllers.crag_controller import crag_controller
from controllers.route_controller import route_controller
from controllers.auth_controller import auth_controller


def create_app():
    app = Flask(__name__)

    @app.errorhandler()
    def validation_error(err):
        return {'error': err.messages}, 400

    # Register the blueprints for the controllers
    app.register_blueprint(crag_controller)
    app.register_blueprint(route_controller)
    app.register_blueprint(auth_controller)

    return app


if __name__ == '__main__':
    app.run(debug=True)
