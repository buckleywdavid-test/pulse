from flask import Flask
from flask_compress import Compress

def create_app(environment='development'):
    app = Flask(__name__, instance_relative_config=True)

    # Gzip compress most things
    app.config['COMPRESS_MIMETYPES'] = [
      'text/html', 'text/css', 'text/xml',
      'text/csv', 'application/json', 'application/javascript'
    ]
    if environment == 'development':
        app.config.from_object('pulse.config.DevelopmentConfig')
    elif environment == 'testing':
        app.config.from_object('pulse.config.TestingConfig')
    else:
        app.config.from_object('pulse.config.ProductionConfig')
    app.config.from_pyfile('application.cfg', silent=True)
    Compress(app)

    from pulse import views
    views.register(app)

    from pulse import helpers
    helpers.register(app)

    return app
