from flask import Flask, request, jsonify
from src.aifl_executor import AIFLExecutor
import logging

app = Flask(__name__)
aifl_executor = AIFLExecutor()

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

@app.route('/')
def home():
    app.logger.debug("Home route accessed")
    return "AIFL Service is Running!"

@app.route('/execute', methods=['POST'])
def execute():
    app.logger.debug(f"Received request: {request.json}")
    data = request.get_json()
    if not data or 'message' not in data:
        app.logger.error("Invalid request: No 'message' field found.")
        return jsonify({'error': "Invalid request: No 'message' field found."}), 400

    aifl_message = data['message']
    app.logger.info(f"Received AIFL message: {aifl_message}")

    try:
        result = aifl_executor.execute(aifl_message)
        app.logger.info(f"Execution result: {result}")
        return jsonify({"result": result}), 200
    except Exception as e:
        app.logger.error(f"Error during execution: {str(e)}", exc_info=True)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.logger.info("Starting Flask server...")
    app.run(host='0.0.0.0', port=8081, debug=True)
