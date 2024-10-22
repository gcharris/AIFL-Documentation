from flask import Flask, request, jsonify, render_template
from flask_talisman import Talisman
from src.aifl_executor import AIFLExecutor
import logging
import os

app = Flask(__name__)
Talisman(app)

aifl_executor = AIFLExecutor()

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute_aifl():
    app.logger.debug(f"Received request: {request.json}")
    data = request.json
    if not data or ('expression' not in data and 'message' not in data):
        app.logger.error("Missing 'expression' or 'message' in request body")
        return jsonify({"error": "Missing 'expression' or 'message' in request body"}), 400

    expression = data.get('expression') or data.get('message')
    try:
        result = aifl_executor.execute(expression)
        app.logger.debug(f"Execution result: {result}")
        return jsonify({"result": result})
    except Exception as e:
        app.logger.error(f"Error during execution: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))  # Changed default port to 8080
    app.run(host='0.0.0.0', port=port, ssl_context='adhoc', debug=True)
