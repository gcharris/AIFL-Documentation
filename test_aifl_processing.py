import unittest
from aifl_executor import AIFLExecutor

class TestAIFLProcessing(unittest.TestCase):
    def setUp(self):
        self.executor = AIFLExecutor()

    def _parse_and_execute(self, expression):
        return self.executor.execute(expression)

    def test_simple_symbol_execution(self):
        result = self._parse_and_execute("ΔΔ1")
        self.assertIn("Executed symbol: ΔΔ1", result)

    def test_simple_operation_execution(self):
        result = self._parse_and_execute("ΔΔ1 ∧ ΔΙ5")
        expected_substrings = [
            "Executed operation: ∧",
            "Executed symbol: ΔΔ1",
            "Executed symbol: ΔΙ5"
        ]
        for substring in expected_substrings:
            self.assertIn(substring, result)

    def test_complex_operation_execution(self):
        result = self._parse_and_execute("ΔΔ1 ∧ ΔΙ5 ⇒ ΔΖ3")
        expected_substrings = [
            "Executed operation: ⇒",
            "Executed operation: ∧",
            "Executed symbol: ΔΔ1",
            "Executed symbol: ΔΙ5",
            "Executed symbol: ΔΖ3"
        ]
        for substring in expected_substrings:
            self.assertIn(substring, result)

    def test_function_execution(self):
        result = self._parse_and_execute("ΔΕ1(Data: 'SensitiveInfo', EncryptionType: 'AES256')")
        expected_substrings = [
            "Executed function: ΔΕ1",
            "Data: SensitiveInfo",
            "EncryptionType: AES256"
        ]
        for substring in expected_substrings:
            self.assertIn(substring, result)

    def test_conditional_execution(self):
        result = self._parse_and_execute("IF(ΔΣ1 > Threshold) THEN ΔΕ1(Data: 'SensitiveInfo') ELSE ΔΑ1(Data: 'PublicInfo')")
        expected_substrings = [
            "Executed conditional:",
            "Executed symbol: ΔΣ1",
            "Executed function: ΔΕ1",
            "Executed function: ΔΑ1"
        ]
        for substring in expected_substrings:
            self.assertIn(substring, result)

    def test_complex_expression_execution(self):
        expr = "ΔΕ1(Data: 'UserCredentials', EncryptionType: 'RSA') ∧ (ΔΘ5α ∧ ΔΜ1) ⇒ ΔΝ2"
        result = self._parse_and_execute(expr)
        expected_substrings = [
            "Executed symbol: ΔΝ2",
            "Executed function: ΔΕ1",
            "Executed symbol: ΔΘ5α",
            "Executed symbol: ΔΜ1"
        ]
        for substring in expected_substrings:
            self.assertIn(substring, result)

if __name__ == '__main__':
    unittest.main()
