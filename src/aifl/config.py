# src/aifl/config.py
import os
from dotenv import load_dotenv

load_dotenv()

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
        import logging
        logging.getLogger('watchdog.observers.inotify_buffer').setLevel(logging.WARNING)

        # Configure Flask
        app.config.from_object(cls)