from flask_sqlalchemy import SQLAlchemy

# Initialize the database instance

db = SQLAlchemy()


def initialize_database(app):
    # Configure the database connection
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://cameronjohn89:JIMbob89@localhost:5432/cameronjohn89'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    # Initialize the database with the Flask app
    db.init_app(app)

    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
