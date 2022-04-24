OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}