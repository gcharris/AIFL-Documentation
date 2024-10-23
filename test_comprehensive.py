# test_comprehensive.py
import unittest
from src.aifl import (
    AIFLParser, 
    AIFLExecutor,
    encrypt_data,
    decrypt_data,
    OpenAIIntegration,
    ClaudeIntegration,
    GeminiIntegration
)

class TestAIFL(unittest.TestCase):
    def setUp(self):
        self.parser = AIFLParser()
        self.executor = AIFLExecutor()
        self.test_expressions = [
            "ΔΕ1(Data: 'TestData', EncryptionType: 'AES256')",
            "ΔΕ1(Data: 'TestData', EncryptionType: 'AES256') ∧ ΔΙ5",
            "ΔΕ1(Data: 'TestData') ⇒ ΔΖ3",
            "IF(ΔΣ1 > Threshold) THEN ΔΕ1(Data: 'SensitiveInfo') ELSE ΔΑ1(Data: 'PublicInfo')"
        ]

    def test_parser(self):
        """Test that the parser can handle various expressions"""
        for expr in self.test_expressions:
            with self.subTest(expr=expr):
                try:
                    result = self.parser.parse(expr)
                    self.assertIsNotNone(result)
                except Exception as e:
                    self.fail(f"Parser failed on expression '{expr}': {str(e)}")

    def test_executor(self):
        """Test that the executor can handle various expressions"""
        for expr in self.test_expressions:
            with self.subTest(expr=expr):
                try:
                    result = self.executor.execute(expr)
                    self.assertIsNotNone(result)
                    print(f"Executed '{expr}': {result}")
                except Exception as e:
                    self.fail(f"Executor failed on expression '{expr}': {str(e)}")

    def test_encryption(self):
        """Test encryption and decryption"""
        test_data = "Sensitive test data"
        try:
            encrypted = encrypt_data(test_data)
            decrypted = decrypt_data(encrypted)
            self.assertEqual(test_data, decrypted)
        except Exception as e:
            self.fail(f"Encryption test failed: {str(e)}")

    def test_ai_integrations(self):
        """Test all AI integrations"""
        integrations = {
            'openai': OpenAIIntegration(),
            'claude': ClaudeIntegration(),
            'gemini': GeminiIntegration()
        }

        test_input = "Test processing input"
        for name, integration in integrations.items():
            with self.subTest(integration=name):
                try:
                    result = integration.process(test_input)
                    self.assertIsInstance(result, dict)
                    self.assertIn('status', result)
                    print(f"{name} integration result: {result}")
                except Exception as e:
                    self.fail(f"{name} integration failed: {str(e)}")

if __name__ == '__main__':
    unittest.main(verbosity=2)