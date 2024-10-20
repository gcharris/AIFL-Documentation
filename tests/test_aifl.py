import unittest
from aifl_parser import AIFLParser
from aifl_executor import AIFLExecutor

class TestAIFL(unittest.TestCase):
    def setUp(self):
        self.parser = AIFLParser()
        self.executor = AIFLExecutor()

    def test_symbol(self):
        expr = "ΔΔ1"
        result = self.executor.execute(expr)
        expected = "Executed symbol: ΔΔ1"
        self.assertEqual(result.strip(), expected)

    def test_conjunction(self):
        expr = "ΔΔ1 ∧ ΔΙ5"
        result = self.executor.execute(expr)
        expected = ("Executed operation: ∧\n"
                    "  Left: Executed symbol: ΔΔ1\n"
                    "  Right: Executed symbol: ΔΙ5")
        self.assertEqual(result.strip(), expected)

    def test_implication(self):
        expr = "ΔΔ1 ∧ ΔΙ5 ⇒ ΔΖ3"
        result = self.executor.execute(expr)
        expected = ("Executed operation: ⇒\n"
                    "  Left:   Executed operation: ∧\n"
                    "    Left: Executed symbol: ΔΔ1\n"
                    "    Right: Executed symbol: ΔΙ5\n"
                    "  Right: Executed symbol: ΔΖ3")
        self.assertEqual(result.strip(), expected)

    def test_function_call(self):
        expr = "ΔΕ1(Data: 'SensitiveInfo', EncryptionType: 'AES256')"
        result = self.executor.execute(expr)
        expected = "Executed function: ΔΕ1(Data: SensitiveInfo, EncryptionType: AES256)"
        self.assertEqual(result.strip(), expected)

    def test_conditional(self):
        expr = "IF(ΔΣ1 > Threshold) THEN ΔΕ1(Data: 'SensitiveInfo') ELSE ΔΑ1(Data: 'PublicInfo')"
        result = self.executor.execute(expr)
        expected = ("Executed conditional:\n"
                    "  Condition: Executed symbol: ΔΣ1 > Threshold\n"
                    "  Then: Executed function: ΔΕ1(Data: SensitiveInfo)\n"
                    "  Else: Executed function: ΔΑ1(Data: PublicInfo)")
        self.assertEqual(result.strip(), expected)

    def test_complex_expression(self):
        expr = "ΔΕ1(Data: 'UserCredentials', EncryptionType: 'RSA') ∧ (ΔΘ5α ∧ ΔΜ1) ⇒ ΔΝ2"
        result = self.executor.execute(expr)
        expected = ("Executed operation: ⇒\n"
                    "  Left:   Executed operation: ∧\n"
                    "    Left: Executed function: ΔΕ1(Data: UserCredentials, EncryptionType: RSA)\n"
                    "    Right:     Executed operation: ∧\n"
                    "      Left: Executed symbol: ΔΘ5α\n"
                    "      Right: Executed symbol: ΔΜ1\n"
                    "  Right: Executed symbol: ΔΝ2")
        self.assertEqual(result.strip(), expected)

if __name__ == '__main__':
    unittest.main()
