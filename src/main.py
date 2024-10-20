# src/main.py

import logging
from encryption import encrypt_data, test_data_encryption
from aifl_symbols import aifl_process_and_generate
from aifl_parser import AIFLParser
from aifl_executor import AIFLExecutor

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    executor = AIFLExecutor()
    expression = "ΔΕ1(Data: 'SensitiveInfo', EncryptionType: 'AES256') ∧ ΔΙ5 ⇒ ΔΖ3"
    try:
        result = executor.execute(expression)
        logger.info(f"Executed result: {result}")
    except Exception as e:
        logger.error(f"Error executing expression: {expression}")
        logger.error(e)

    demonstrate_advanced_aifl()

    # Test data encryption
    encryption_test_result, test_data, encrypted_data = test_data_encryption()

    if encryption_test_result:
        logger.info(f"ΣΑ1 ⇒ Data Encryption (ΔΕ1) test passed. Original: '{test_data}', Encrypted: '{encrypted_data}'")

        # Proceed with the main process if encryption test passes
        input_data = "Explain the concept of AIFL in the context of AI development, including data encryption and advanced parsing capabilities"
        try:
            result = aifl_process_and_generate(input_data)
            logger.info(f"Input: {input_data}")
            logger.info(f"AIFL-processed output: {result}")
        except Exception as e:
            logger.error(f"Error processing input data: {input_data}")
            logger.error(e)
    else:
        logger.error("ΦΗ7δ ⇒ Encryption test failed. Aborting main process.")

def demonstrate_advanced_aifl():
    parser = AIFLParser()
    executor = AIFLExecutor()
    advanced_expressions = [
        "ΔΔ1 ∧ ΔΙ5 ⇒ ΔΖ3",
        "IF(ΔΣ1 > Threshold) THEN ΔΕ1(Data: 'SensitiveInfo') ELSE ΔΑ1(Data: 'PublicInfo')",
        "ΔΕ1(Data: 'UserCredentials', EncryptionType: 'RSA') ∧ (ΔΘ5α ∧ ΔΜ1) ⇒ ΔΝ2",
        "ΔΔ1(Data: 'Explain the concept of AIFL in the context of AI development, including data encryption and advanced parsing capabilities')"
    ]

    for expr in advanced_expressions:
        logger.info(f"Parsing and executing advanced AIFL expression: {expr}")
        try:
            parsed_result = parser.parse(expr)
            logger.info(f"Parsed result: {parsed_result}")

            executed_result = executor.execute(expr)
            logger.info(f"Executed result: {executed_result}")
        except Exception as e:
            logger.error(f"Error parsing or executing expression: {e}")
        logger.info("---")

if __name__ == "__main__":
    main()
