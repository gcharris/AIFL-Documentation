# tests/test_parser.py

import unittest
from src.aifl_executor import AIFLExecutor
from src.aifl_parser import AIFLParser

class TestAIFLParser(unittest.TestCase):
    def setUp(self):
        self.parser = AIFLParser()
        self.executor = AIFLExecutor()

    def test_parser_and_executor(self):
        expressions = [
            "ΔΔ1",
            "ΔΔ1 ∧ ΔΙ5",
            "ΔΔ1 ∧ ΔΙ5 ⇒ ΔΖ3",
            "ΔΕ1(Data: 'SensitiveInfo', EncryptionType: 'AES256')",
            "IF(ΔΣ1 > Threshold) THEN ΔΕ1(Data: 'SensitiveInfo') ELSE ΔΑ1(Data: 'PublicInfo')",
            "ΔΕ1(Data: 'UserCredentials', EncryptionType: 'RSA') ∧ (ΔΘ5α ∨ ΔΜ1) ⇒ ΔΝ2"
        ]

        for expr in expressions:
            with self.subTest(expr=expr):
                try:
                    parsed = self.parser.parse(expr)
                    self.assertIsNotNone(parsed, f"Parsing failed for expression: {expr}")

                    executed = self.executor.execute(expr)
                    self.assertIsNotNone(executed, f"Execution failed for expression: {expr}")
                except Exception as e:
                    self.fail(f"Error for expression '{expr}': {str(e)}")
