# src/app.py
from flask import Flask, request, jsonify
import os
import logging

# Configure logging first
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

# Configuration
app.config.update(
    DEBUG=True,
    SECRET_KEY=os.getenv('SECRET_KEY', 'dev-key-please-change'),
    ENV='development'
)

# Initialize components
parser = AIFLParser()
executor = AIFLExecutor()

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
        'endpoints': {
            '/': 'This help message',
            '/health': 'Server health check',
            '/execute': 'Execute AIFL expressions'
        }
    })

@app.route('/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'available_ai_providers': list(ai_integrations.keys()),
        'components': {
            'parser': bool(parser),
            'executor': bool(executor)
        }
    })

@app.route('/execute', methods=['POST'])
def execute_aifl():
    try:
        data = request.get_json()
        if not data or 'expression' not in data:
            return jsonify({
                'status': 'error',
                'message': 'Missing AIFL expression in request'
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
                'message': f'Error processing AIFL expression: {str(e)}'
            }), 400

        # Process with AI provider
        if ai_provider in ai_integrations:
            ai_result = ai_integrations[ai_provider].process(executed_result)
        else:
            return jsonify({
                'status': 'error',
                'message': f'Unknown AI provider: {ai_provider}'
            }), 400

        return jsonify({
            'status': 'success',
            'parsed_result': str(parsed_result),
            'executed_result': executed_result,
            'ai_result': ai_result
        })

    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    # Get port from environment or use 3000 as default
    port = int(os.getenv('PORT', 3000))

    # Start server
    app.run(
        host='0.0.0.0',
        port=port,
        debug=True
    )