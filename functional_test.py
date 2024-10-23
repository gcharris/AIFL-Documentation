# functional_test.py
import logging
import sys
from typing import Dict, Any
from src.aifl import (
    AIFLParser,
    AIFLExecutor,
    OpenAIIntegration,
    ClaudeIntegration,
    GeminiIntegration,
    encrypt_data,
    decrypt_data
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def test_parser_executor() -> bool:
    """Test AIFL parser and executor functionality"""
    try:
        logger.info("Testing AIFL Parser and Executor...")
        parser = AIFLParser()
        executor = AIFLExecutor()

        test_expressions = [
            "ΔΕ1(Data: 'TestData', EncryptionType: 'AES256')",
            "ΔΕ1(Data: 'TestData') ∧ ΔΙ5",
            "ΔΕ1(Data: 'TestData') ⇒ ΔΖ3"
        ]

        for expr in test_expressions:
            logger.info(f"\nTesting expression: {expr}")
            parsed = parser.parse(expr)
            logger.info(f"Parsed result: {parsed}")

            executed = executor.execute(expr)
            logger.info(f"Executed result: {executed}")

        return True
    except Exception as e:
        logger.error(f"Parser/Executor test failed: {str(e)}")
        return False

def test_encryption() -> bool:
    """Test encryption functionality"""
    try:
        logger.info("\nTesting encryption...")
        test_data = "Sensitive test data"
        encrypted = encrypt_data(test_data)
        logger.info(f"Encrypted data: {encrypted}")

        decrypted = decrypt_data(encrypted)
        logger.info(f"Decrypted data: {decrypted}")

        assert decrypted == test_data, "Decryption failed"
        return True
    except Exception as e:
        logger.error(f"Encryption test failed: {str(e)}")
        return False

def test_ai_integrations() -> Dict[str, bool]:
    """Test all AI integrations"""
    results = {}
    integrations = {
        'OpenAI': OpenAIIntegration(),
        'Claude': ClaudeIntegration(),
        'Gemini': GeminiIntegration()
    }

    test_input = "Test AI processing input"

    for name, integration in integrations.items():
        try:
            logger.info(f"\nTesting {name} integration...")
            result = integration.process(test_input)
            logger.info(f"{name} result: {result}")
            results[name] = True
        except Exception as e:
            logger.error(f"{name} integration test failed: {str(e)}")
            results[name] = False

    return results

def run_all_tests():
    """Run all functional tests and report results"""
    logger.info("Starting AIFL functional tests...")

    results = {
        'Parser/Executor': test_parser_executor(),
        'Encryption': test_encryption(),
        'AI Integrations': test_ai_integrations()
    }

    logger.info("\n=== Test Results ===")
    all_passed = True
    for component, result in results.items():
        if isinstance(result, dict):  # AI integration results
            for ai, ai_result in result.items():
                status = "✓" if ai_result else "✗"
                logger.info(f"{status} {component} - {ai}")
                all_passed = all_passed and ai_result
        else:
            status = "✓" if result else "✗"
            logger.info(f"{status} {component}")
            all_passed = all_passed and result

    return all_passed

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)