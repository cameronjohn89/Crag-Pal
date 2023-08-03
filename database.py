
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Initialize the database instance
db = SQLAlchemy()

def initialize_database(app):
    # Set the configuration based on the environment (e.g., development, production)
    app.config.from_object(Config)

    # Initialize the database with the Flask app
    db.init_app(app)

    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
