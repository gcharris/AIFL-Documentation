import os
import openai
import logging
from typing import Dict, Any

class OpenAIIntegration:
    def __init__(self):
        self.logger = logging.getLogger('AIFL.OpenAIIntegration')
        self.api_key = os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            self.logger.error("OpenAI API key not found in environment variables")
            raise ValueError("OpenAI API key not found")

        openai.api_key = self.api_key

    def process(self, executed_result: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process the executed AIFL result using OpenAI's API.

        Args:
            executed_result: The result from the AIFL executor

        Returns:
            Dict containing the processing results
        """
        try:
            self.logger.info(f"Processing result with OpenAI: {executed_result}")

            # Construct the messages for OpenAI
            messages = self._construct_messages(executed_result)

            # Call OpenAI API with v0.27.0 syntax
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.7
            )

            # Extract and format the response
            ai_response = response.choices[0].message.content

            return {
                "status": "success",
                "result": ai_response,
                "model": "gpt-3.5-turbo"
            }

        except Exception as e:
            self.logger.error(f"Error processing with OpenAI: {str(e)}")
            return {
                "status": "error",
                "error": str(e),
                "model": "gpt-3.5-turbo"
            }

    def _construct_messages(self, executed_result: Dict[str, Any]) -> list:
        """
        Construct messages list for OpenAI API based on the executed result.

        Args:
            executed_result: The result from the AIFL executor

        Returns:
            list: List of message dictionaries
        """
        # System message
        system_message = {
            "role": "system",
            "content": """You are an AI assistant helping to process AIFL 
            (AI Foundational Language) commands. Your role is to analyze AIFL commands 
            and provide appropriate responses based on the command type and parameters."""
        }

        # Construct user message based on result type
        if isinstance(executed_result, dict):
            if executed_result.get('type') == 'symbol_call':
                symbol = executed_result.get('symbol', '')
                params = executed_result.get('parameters', {})

                user_content = f"""
                Analyze and respond to the following AIFL command:
                Symbol: {symbol}
                Parameters: {params}

                Based on the AIFL specification:
                1. What is the purpose of this command?
                2. What actions should be taken?
                3. What would be an appropriate response?

                Format your response in a clear and concise manner.
                """

            elif executed_result.get('type') == 'operation':
                operator = executed_result.get('operator', '')
                left = executed_result.get('left', {})
                right = executed_result.get('right', {})

                user_content = f"""
                Analyze and respond to the following AIFL operation:
                Operator: {operator}
                Left operand: {left}
                Right operand: {right}

                Based on the AIFL specification:
                1. What is this operation trying to achieve?
                2. How should the operands be combined?
                3. What would be an appropriate response?

                Format your response in a clear and concise manner.
                """

            else:
                user_content = f"Analyze and provide an appropriate response for this AIFL result: {executed_result}"
        else:
            user_content = f"Analyze and provide an appropriate response for this AIFL result: {executed_result}"

        user_message = {
            "role": "user",
            "content": user_content.strip()
        }

        return [system_message, user_message]