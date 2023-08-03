
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://cameronjohn89:JIMbob89@localhost:5432/cameronjohn89'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # Add any other configuration variables here

class DevelopmentConfig(Config):
    DEBUG = True
    # Add development-specific configuration variables here

class ProductionConfig(Config):
    DEBUG = False
    # Add production-specific configuration variables here

# You can add more configurations for other environments (testing, staging, etc.) if needed.
