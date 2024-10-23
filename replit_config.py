# replit_config.py
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class ReplitConfig:
    # Replit-specific settings
    PORT = 3000  # Replit prefers port 3000
    HOST = '0.0.0.0'  # Required for Replit

    # Flask settings
    DEBUG = True
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-here')

    # AIFL settings
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    CLAUDE_API_KEY = os.getenv('CLAUDE_API_KEY')
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

    # URLs and endpoints
    BASE_URL = os.getenv('REPLIT_URL', 'https://{}.repl.co').format(
        os.getenv('REPL_SLUG', 'your-repl-name')
    )

    @classmethod
    def get_url(cls, endpoint: str) -> str:
        """Get full URL for endpoint"""
        return f"{cls.BASE_URL}{endpoint}"

# Update app.py to use Replit configuration
REPLIT_CONFIG = ReplitConfig()