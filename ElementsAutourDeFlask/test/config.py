# Sera utilisé pour configurer la db
basedir  = os.getcwd()
basedir = basedir[0] if isinstance(basedir, list) else basedir

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False