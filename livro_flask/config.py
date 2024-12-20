import os
import random, string
class Config(object):
    CSRF_ENABLED = True
    SECRET = 'ysb_92=qe#djf8%ng+a*#4rt#5%3*4k5%i2bck*gn@w3@f&-&'
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    APP = None
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://user:passwd@host:port/database'
class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = '127.0.0.1'
    PORT_HOST = 8000
    URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)
class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = '127.0.0.1' # Aqui geralmente é um IP de um servidor na nuvem e não o endereço da máquina local
    PORT_HOST = 5000
    URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)
class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    IP_HOST = '127.0.0.1' # Aqui geralmente é um IP de um servidor na nuvem e não o endereço da máquina local
    PORT_HOST = 8080
    URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)
    
app_config = {
'development': DevelopmentConfig(),
'testing': TestingConfig(),
'production': ProductionConfig()
}
app_active = os.getenv('FLASK_ENV')

#export FLASK_ENV=development 