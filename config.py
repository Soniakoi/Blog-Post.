
class Config:
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://sonia:sonia@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

class ProdConfig(Config):
    pass

class TestConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options ={"production":ProdConfig,"default":DevConfig,"testing":TestConfig}

