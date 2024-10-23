# src/aifl/config.py
import os
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Remove deprecated FLASK_ENV
if 'FLASK_ENV' in os.environ:
    del os.environ['FLASK_ENV']
os.environ['FLASK_DEBUG'] = '1'

class FlaskConfig:
    # Flask settings
    DEBUG = True  # Instead of FLASK_ENV=development
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-change-this')

    # Server settings
    PORT = 3000  # Replit preferred port
    HOST = '0.0.0.0'  # Required for Replit

    # Logging settings
    LOG_LEVEL = 'INFO'  # Reduce debug noise
    PROPAGATE_EXCEPTIONS = True

    # AIFL settings
    AIFL_ENV = 'development'
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

    @classmethod
    def init_app(cls, app):
        # Configure logging
        logging.getLogger('watchdog.observers.inotify_buffer').setLevel(logging.WARNING)

        # Disable Flask environment deprecation warning
        if 'FLASK_ENV' in os.environ:
            del os.environ['FLASK_ENV']
        os.environ['FLASK_DEBUG'] = '1'

        # Configure Flask
        app.config.from_object(cls)