# run.py
import os
import sys

# Add the src directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from app import app

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)