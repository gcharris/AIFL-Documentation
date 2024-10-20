import unittest
from src.aifl_executor import AIFLExecutor

class TestAIFLProcessing(unittest.TestCase):
    def setUp(self):
        self.executor = AIFLExecutor()

    def test_simple_symbol_execution(self):
        result = self.executor.execute("ΔΔ1")
        self.assertEqual(result, "Executed symbol: ΔΔ1")

    def test_simple_operation_execution(self):
        result = self.executor.execute("ΔΔ1 ∧ ΔΙ5")
        self.assertEqual(result, "Executed operation: ∧ on Executed symbol: ΔΔ1 and Executed symbol: ΔΙ5")

    def test_complex_operation_execution(self):
        result = self.executor.execute("ΔΔ1 ∧ ΔΙ5 ⇒ ΔΖ3")
        self.assertEqual(result, "Executed operation: ⇒ on Executed operation: ∧ on Executed symbol: ΔΔ1 and Executed symbol: ΔΙ5 and Executed symbol: ΔΖ3")

    def test_function_execution(self):
        result = self.executor.execute("ΔΕ1(Data: 'SensitiveInfo', EncryptionType: 'AES256')")
        self.assertEqual(result, "Executed function: ΔΕ1(Data: SensitiveInfo, EncryptionType: AES256)")

    def test_conditional_execution(self):
        result = self.executor.execute("IF(ΔΣ1 > Threshold) THEN ΔΕ1(Data: 'SensitiveInfo') ELSE ΔΑ1(Data: 'PublicInfo')")
        expected = "Executed conditional: IF Executed operation: > on Executed symbol: ΔΣ1 and Threshold THEN Executed function: ΔΕ1(Data: SensitiveInfo) ELSE Executed function: ΔΑ1(Data: PublicInfo)"
        self.assertEqual(result, expected)

    def test_nested_operations(self):
        result = self.executor.execute("(ΔΔ1 ∧ ΔΙ5) ∨ (ΔΖ3 ∧ ΔΘ5α)")
        expected = "Executed operation: ∨ on Executed operation: ∧ on Executed symbol: ΔΔ1 and Executed symbol: ΔΙ5 and Executed operation: ∧ on Executed symbol: ΔΖ3 and Executed symbol: ΔΘ5α"
        self.assertEqual(result, expected)

    def test_complex_expression(self):
        result = self.executor.execute("IF(ΔΕ1(Data: 'UserCredentials') ∧ (ΔΘ5α ∨ ΔΜ1)) THEN ΔΝ2 ELSE ΔΑ1")
        expected = "Executed conditional: IF Executed operation: ∧ on Executed function: ΔΕ1(Data: UserCredentials) and Executed operation: ∨ on Executed symbol: ΔΘ5α and Executed symbol: ΔΜ1 THEN Executed symbol: ΔΝ2 ELSE Executed symbol: ΔΑ1"
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
