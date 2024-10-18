import logging
from encryption import encrypt_data, test_data_encryption
from aifl_symbols import aifl_process_and_generate

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    # Test data encryption
    encryption_test_result, test_data, encrypted_data = test_data_encryption()
    
    if encryption_test_result:
        logger.info(f"ΣΑ1 ⇒ Data Encryption (ΔΕ1) test passed. Original: '{test_data}', Encrypted: '{encrypted_data}'")
        
        # Proceed with the main process if encryption test passes
        input_data = "Explain the concept of AIFL in the context of AI development, including data encryption"
        result = aifl_process_and_generate(input_data, encrypted_data)
        logger.info(f"Input: {input_data}")
        logger.info(f"AIFL-processed output: {result}")
    else:
        logger.error("ΦΗ7δ ⇒ Encryption test failed. Aborting main process.")
