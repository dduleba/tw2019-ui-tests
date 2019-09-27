import os


def get_conduit_dir():
    return os.path.abspath(os.path.dirname(__file__))


def get_conduit_etc_dir():
    return os.path.join(get_conduit_dir(), 'etc')


def get_etc_dir():
    return get_conduit_etc_dir()
