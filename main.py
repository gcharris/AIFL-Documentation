import os
from flask import Flask, request, jsonify, render_template
import logging
from werkzeug.middleware.proxy_fix import ProxyFix
from werkzeug.urls import url_parse

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

@app.before_request
def before_request():
    # Redirect HTTP to HTTPS
    if not request.is_secure and not app.debug:
        url = request.url.replace('http://', 'https://', 1)
        return redirect(url, code=301)

@app.after_request
def add_security_headers(response):
    # Add security headers
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute():
    data = request.get_json()
    if not data or 'message' not in data:
        logging.error("Invalid request: No 'message' field found.")
        return jsonify({'error': "Invalid request: No 'message' field found."}), 400

    aifl_message = data['message']
    logging.info(f"Received AIFL message: {aifl_message}")

    try:
        result = {"result": f"Processed message: {aifl_message}"}
        logging.info(f"Execution result: {result}")
        return jsonify(result), 200

    except Exception as e:
        logging.error(f"Error processing message: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8081))
    app.run(host='0.0.0.0', port=port, ssl_context='adhoc', debug=True)
