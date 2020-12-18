import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Dev(object):
    TESTING = True
    DEBUG = True
    HOST = "0.0.0.0"