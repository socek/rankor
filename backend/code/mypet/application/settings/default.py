from os import environ

from sapp.plugins.settings import PrefixedStringsDict


def default():
    settings = {
        'paths': PrefixedStringsDict('/code/'),
    }
    logging(settings)
    database(settings)
    return settings


def logging(settings):
    settings['logging'] = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'generic': {
                'format':
                '%(asctime)s %(levelname)-5.5s [%(name)s][%(threadName)s] %(message)s',
            },
        },
        'handlers': {
            'console': {
                'level': "DEBUG",
                'class': 'logging.StreamHandler',
                'formatter': 'generic',
            },
        },
        'loggers': {
            '': {
                'level': 'DEBUG',
                'handlers': [],
            },
            'sqlalchemy': {
                'level': 'ERROR',
                'handlers': ['console'],
                'qualname': 'sqlalchemy.engine',
            },
            'alembic': {
                'level': 'ERROR',
                'handlers': ['console'],
                'qualname': 'alembic',
            },
            'ccads': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'qualname': 'ccads',
            },
            'waitress': {
                'level': 'ERROR',
                'handlers': ['console'],
            },
            'celery': {
                'handlers': ['console'],
                'level': 'ERROR',
            },
        }
    }


def database(settings):
    settings['db:dbsession:url'] = environ['BACKEND_DB_URL']
    settings['db:dbsession:default_url'] = environ['BACKEND_DB_DEFAULT_URL']
