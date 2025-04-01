import os
import logging
import logging.config

def setup_logging():
    log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
    log_format = os.getenv('LOG_FORMAT', '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    logging_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                'format': log_format,
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'default',
                'level': log_level,
            },
        },
        'root': {
            'handlers': ['console'],
            'level': log_level,
        },
    }

    logging.config.dictConfig(logging_config)
