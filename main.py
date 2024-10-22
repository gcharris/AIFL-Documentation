from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

@app.route('/')
def home():
    return "AIFL Service is Running!"

@app.route('/execute', methods=['POST'])
def execute():
    data = request.get_json()
    if not data or 'message' not in data:
        logging.error("Invalid request: No 'message' field found.")
        return jsonify({'error': "Invalid request: No 'message' field found."}), 400

    aifl_message = data['message']
    logging.info(f"Received AIFL message: {aifl_message}")

    # TODO: Integrate your parser and executor here
    # For demonstration, we'll echo back the message
    result = {"result": f"Processed message: {aifl_message}"}

    logging.info(f"Execution result: {result}")
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
