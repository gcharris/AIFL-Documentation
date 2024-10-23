# src/app.py
from flask import Flask, request, jsonify
import os
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Import AIFL components
try:
    from aifl import (
        AIFLParser,
        AIFLExecutor,
        OpenAIIntegration,
        ClaudeIntegration,
        GeminiIntegration
    )
except ImportError as e:
    logger.error(f"Failed to import AIFL components: {str(e)}")
    raise

app = Flask(__name__)

# Updated configuration without deprecated FLASK_ENV
app.config.update(
    DEBUG=os.getenv('FLASK_DEBUG', '1') == '1',
    SECRET_KEY=os.getenv('SECRET_KEY', 'dev-key-please-change'),
    JSON_SORT_KEYS=False  # Preserve JSON order for readability
)

# Initialize components
parser = AIFLParser()
executor = AIFLExecutor()
start_time = datetime.utcnow()

# Initialize AI integrations
ai_integrations = {
    'openai': OpenAIIntegration(),
    'claude': ClaudeIntegration(),
    'gemini': GeminiIntegration()
}

@app.route('/')
def home():
    return jsonify({
        'status': 'success',
        'message': 'AIFL API is running',
        'version': '0.1.0',
        'uptime': str(datetime.utcnow() - start_time),
        'endpoints': {
            '/': 'API information',
            '/health': 'System health status',
            '/execute': 'Execute AIFL expressions (POST)',
            '/docs': 'API documentation (coming soon)'
        }
    })

@app.route('/health')
def health_check():
    uptime = datetime.utcnow() - start_time
    return jsonify({
        'status': 'healthy',
        'uptime': str(uptime),
        'available_ai_providers': list(ai_integrations.keys()),
        'components': {
            'parser': bool(parser),
            'executor': bool(executor)
        },
        'system': {
            'debug_mode': app.debug,
            'environment': os.getenv('FLASK_DEBUG', 'development')
        }
    })

@app.route('/execute', methods=['POST'])
def execute_aifl():
    try:
        data = request.get_json()
        if not data or 'expression' not in data:
            return jsonify({
                'status': 'error',
                'message': 'Missing AIFL expression in request',
                'timestamp': datetime.utcnow().isoformat()
            }), 400

        expression = data['expression']
        ai_provider = data.get('ai_provider', 'openai')

        logger.info(f"Processing AIFL expression: {expression}")

        # Parse and execute
        try:
            parsed_result = parser.parse(expression)
            executed_result = executor.execute(expression)
        except Exception as e:
            logger.error(f"Processing error: {str(e)}")
            return jsonify({
                'status': 'error',
                'message': f'Error processing AIFL expression: {str(e)}',
                'timestamp': datetime.utcnow().isoformat()
            }), 400

        # Process with AI provider
        if ai_provider in ai_integrations:
            ai_result = ai_integrations[ai_provider].process(executed_result)
        else:
            return jsonify({
                'status': 'error',
                'message': f'Unknown AI provider: {ai_provider}',
                'available_providers': list(ai_integrations.keys()),
                'timestamp': datetime.utcnow().isoformat()
            }), 400

        return jsonify({
            'status': 'success',
            'parsed_result': str(parsed_result),
            'executed_result': executed_result,
            'ai_result': ai_result,
            'timestamp': datetime.utcnow().isoformat()
        })

    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': str(e),
            'timestamp': datetime.utcnow().isoformat()
        }), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 3000))

    # Start message
    logger.info(f"Starting AIFL API server on port {port}")
    logger.info(f"Debug mode: {app.debug}")

    # Run server
    app.run(
        host='0.0.0.0',
        port=port,
        debug=app.debug
    )