import os

APP_ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
PERSISTENCE_ENGINE = 'Mongo'
OS_SEPARATOR = os.sep


def set_persistence_engine(engine):
    global PERSISTENCE_ENGINE
    PERSISTENCE_ENGINE = engine
