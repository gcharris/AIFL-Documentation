from flask import Flask, request, jsonify, render_template
from src.aifl_executor import AIFLExecutor
import logging

app = Flask(__name__)
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
    if not data or 'expression' not in data:
        app.logger.error("Missing 'expression' in request body")
        return jsonify({"error": "Missing 'expression' in request body"}), 400

    expression = data['expression']
    try:
        result = aifl_executor.execute(expression)
        app.logger.debug(f"Execution result: {result}")
        return jsonify({"result": result})
    except Exception as e:
        app.logger.error(f"Error during execution: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
