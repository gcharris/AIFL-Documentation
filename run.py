# run.py
from src.app import app

if __name__ == "__main__":
    print("\nStarting AIFL server on port 3001...")
    app.run(
        host='0.0.0.0',
        port=3001,
        debug=False  # Disable debug mode for now
    )