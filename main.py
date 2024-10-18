import logging
from encryption import encrypt_data, test_data_encryption
from aifl_symbols import aifl_process_and_generate
from aifl_parser import AIFLParser

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def demonstrate_advanced_aifl():
    parser = AIFLParser()
    advanced_expressions = [
        "ΔΔ1 ∧ ΔΙ5 ⇒ ΔΖ3",
        "IF(ΔΣ1 > Threshold) THEN ΔΕ1(Data: 'SensitiveInfo') ELSE ΔΑ1(Data: 'PublicInfo')",
        "ΔΕ1(Data: 'UserCredentials', EncryptionType: 'RSA') ∧ (ΔΘ5α ∧ ΔΜ1) ⇒ ΔΝ2"
    ]

    for expr in advanced_expressions:
        logger.info(f"Parsing advanced AIFL expression: {expr}")
        try:
            result = parser.parse(expr)
            logger.info(f"Parsed result: {result}")
        except ValueError as e:
            logger.error(f"Error parsing expression: {e}")
        logger.info("---")

if __name__ == "__main__":
    # Test data encryption
    encryption_test_result, test_data, encrypted_data = test_data_encryption()
    
    if encryption_test_result:
        logger.info(f"ΣΑ1 ⇒ Data Encryption (ΔΕ1) test passed. Original: '{test_data}', Encrypted: '{encrypted_data}'")
        
        # Demonstrate advanced AIFL parsing
        demonstrate_advanced_aifl()
        
        # Proceed with the main process if encryption test passes
        input_data = "Explain the concept of AIFL in the context of AI development, including data encryption and advanced parsing capabilities"
        result = aifl_process_and_generate(input_data)
        logger.info(f"Input: {input_data}")
        logger.info(f"AIFL-processed output: {result}")
    else:
        logger.error("ΦΗ7δ ⇒ Encryption test failed. Aborting main process.")
