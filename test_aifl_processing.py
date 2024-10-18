import unittest
from unittest.mock import patch
from aifl_symbols import aifl_process_and_generate

class TestAIFLProcessing(unittest.TestCase):
    @patch('aifl_symbols.openai.ChatCompletion.create')
    def test_aifl_process_success(self, mock_openai):
        # Mock the API response
        mock_openai.return_value.choices = [
            unittest.mock.Mock(
                message=unittest.mock.Mock(
                    content='ΔΔ1: Retrieve Data\nΔΙ5: Normalize Data\nΔΖ3: Transform Data\nΔΕ1: Encrypt Data\nΔΘ5α: Supervised Learning\nΔΜ1: Train Model\nΔΝ2: Model Evaluation'
                )
            )
        ]
        
        input_data = "Explain the concept of AIFL in the context of AI development, including data encryption"
        result = aifl_process_and_generate(input_data)
        
        self.assertTrue(result.startswith("ΣΑ1 ⇒"))
        self.assertIn("ΔΔ1", result)
        self.assertIn("ΔΙ5", result)
        self.assertIn("ΔΖ3", result)
        self.assertIn("ΔΕ1", result)
        self.assertIn("ΔΘ5α", result)
        self.assertIn("ΔΜ1", result)
        self.assertIn("ΔΝ2", result)

    @patch('aifl_symbols.openai.ChatCompletion.create')
    def test_aifl_process_api_exception(self, mock_openai):
        mock_openai.side_effect = Exception("API Error")
        
        input_data = "Test input"
        result = aifl_process_and_generate(input_data)
        
        self.assertTrue(result.startswith("ΦΗ7δ ⇒ Error:"))
        self.assertIn("API Error", result)

if __name__ == '__main__':
    unittest.main()
