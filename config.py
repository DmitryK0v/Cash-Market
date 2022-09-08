
import logging


DB_NAME = "data/exchange.db"

LOGGER_CONFIG = dict(level=logging.DEBUG,
                     file="data/app.log",
                     formatter=logging.Formatter("%(asctime)s [%(levelname)s] - %(name)s:%(message)s")
                     )
HTTP_TIMEOUT = 15
IP_LIST = ["127.0.0.1", "127.0.0.10"]

LOGGING = {
    'version': 1,
    'formatters': {
        'default': {
            'format': "[%(asctime)s] [%(levelname)s] - %(name)s: %(message)s",
        },
    },

    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'formatter': 'default',
            'filename': 'data/new.log',
        },
    },
    'loggers': {
        'Cash-Market': {
            'handlers': ['file', ],
            'level': logging.DEBUG
        },
        'Api': {
            'handlers': ['file', ],
            'level': logging.DEBUG
        },
        'Tasks': {
            'handlers': ['file', ],
            'level': logging.DEBUG
        },
    },
}