class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:1@localhost:3306/test1'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{}:{}@{}/{}{}'.format("root", "1", "localhost:3306", "test1", "")
    SECRET_KEY = 'something very secret'

    ### Flask_security
    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'
