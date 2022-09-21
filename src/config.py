from decouple import config
import sys
sys.dont_write_bytecode = True

class Config:
    SECRET_KEY=config('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI=config('DATABASE_URL')

class DevelopmentConfig(Config):
    DEBUG =  True

config = {'development': DevelopmentConfig}
