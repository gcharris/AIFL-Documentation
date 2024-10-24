import logging
import os
from openai import OpenAI
from aifl_parser import AIFLParser

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the OpenAI client
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def aifl_process_and_generate(input_data):
    """
    Process input data using AIFL symbols and generate text using OpenAI API.
    """
    parser = AIFLParser()
    
    # AIFL symbols for data processing
    processed_data = f"ΔΔ1('{input_data}') ∧ ΔΙ5 ⇒ ΔΖ3"
    try:
        parsed_processed_data = parser.parse(processed_data)
    except ValueError as e:
        logger.error(f"Error parsing processed data: {e}")
        parsed_processed_data = "Error in parsing"
    
    # AIFL symbol for data encryption
    encryption_step = f"ΔΕ1('{input_data}')"
    try:
        parsed_encryption_step = parser.parse(encryption_step)
    except ValueError as e:
        logger.error(f"Error parsing encryption step: {e}")
        parsed_encryption_step = "Error in parsing"
    
    # AIFL symbols for model invocation
    model_invocation = f"ΔΘ5α ∧ ΔΜ1 ⇒ ΔΝ2"
    try:
        parsed_model_invocation = parser.parse(model_invocation)
    except ValueError as e:
        logger.error(f"Error parsing model invocation: {e}")
        parsed_model_invocation = "Error in parsing"
    
    # Combine AIFL symbols to create a prompt with explanations
    aifl_prompt = f"""
    Given the AIFL process: {processed_data} ∧ {encryption_step} and {model_invocation}, generate a response.
    
    Parsed representations:
    1. Data Processing: {parsed_processed_data}
    2. Data Encryption: {parsed_encryption_step}
    3. Model Invocation: {parsed_model_invocation}
    
    Provide both a concise symbol representation and a detailed explanation for each AIFL symbol used:

    1. ΔΔ1 (Retrieve Data)
    2. ΔΙ5 (Normalize Data)
    3. ΔΖ3 (Transform Data)
    4. ΔΕ1 (Encrypt Data)
    5. ΔΘ5α (Supervised Learning)
    6. ΔΜ1 (Train Model)
    7. ΔΝ2 (Model Evaluation)
    
    For each symbol, include:
    - Concise representation (symbol and brief definition)
    - Detailed explanation (including rationale and example usage)
    
    Using these AIFL symbols and their parsed representations, explain the concept of AIFL in the context of AI development,
    including the importance of data encryption (ΔΕ1) in the process.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an AI assistant that understands AIFL symbols and their parsed representations. Interpret the AIFL process and respond with both concise and detailed explanations for each symbol."},
                {"role": "user", "content": aifl_prompt}
            ],
            max_tokens=1000
        )
        result = response.choices[0].message.content.strip()
        
        # AIFL symbol for successful operation
        logger.info("ΣΑ1 ⇒ Successfully generated AIFL response")
        return f"ΣΑ1 ⇒ {result}"
    except Exception as e:
        # Handle all exceptions
        error_message = f"ΦΗ7δ ⇒ Error: {str(e)}"
        logger.error(error_message)
        return error_message

# Example usage
if __name__ == "__main__":
    input_data = "Explain the concept of AIFL in the context of AI development, including data encryption"
    result = aifl_process_and_generate(input_data)
    print(result)
