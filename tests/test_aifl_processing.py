# tests/test_aifl_processing.py

import unittest
from src.aifl_executor import AIFLExecutor

class TestAIFLProcessing(unittest.TestCase):
    def setUp(self):
        self.executor = AIFLExecutor()

    def test_complex_expression(self):
        expr = "IF(ΔΕ1(Data: 'UserCredentials') ∧ (ΔΘ5α ∨ ΔΜ1)) THEN ΔΝ2 ELSE ΔΑ1"
        result = self.executor.execute(expr)
        expected = "Executed conditional: IF Executed operation: ∧ on Executed function: ΔΕ1(Data: UserCredentials) and Executed operation: ∨ on Executed symbol: ΔΘ5α and Executed symbol: ΔΜ1 THEN Executed symbol: ΔΝ2 ELSE Executed symbol: ΔΑ1"
        self.assertEqual(result, expected)

    def test_complex_operation_execution(self):
        expr = "ΔΔ1 ∧ ΔΙ5 ⇒ ΔΖ3"
        result = self.executor.execute(expr)
        expected = "Executed operation: ⇒ on Executed operation: ∧ on Executed symbol: ΔΔ1 and Executed symbol: ΔΙ5 and Executed symbol: ΔΖ3"
        self.assertEqual(result, expected)

    def test_conditional_execution(self):
        expr = "IF(ΔΣ1 > Threshold) THEN ΔΕ1(Data: 'SensitiveInfo') ELSE ΔΑ1(Data: 'PublicInfo')"
        expected = "Executed conditional: IF Executed operation: > on Executed symbol: ΔΣ1 and Executed symbol: Threshold THEN Executed function: ΔΕ1(Data: SensitiveInfo) ELSE Executed function: ΔΑ1(Data: PublicInfo)"
        result = self.executor.execute(expr)
        self.assertEqual(result, expected)

    def test_function_execution(self):
        expr = "ΔΕ1(Data: 'SensitiveInfo', EncryptionType: 'AES256')"
        result = self.executor.execute(expr)
        expected = "Executed function: ΔΕ1(Data: SensitiveInfo, EncryptionType: AES256)"
        self.assertEqual(result, expected)

    def test_nested_operations(self):
        expr = "(ΔΔ1 ∧ ΔΙ5) ∨ (ΔΖ3 ∧ ΔΘ5α)"
        expected = "Executed operation: ∨ on Executed operation: ∧ on Executed symbol: ΔΔ1 and Executed symbol: ΔΙ5 and Executed operation: ∧ on Executed symbol: ΔΖ3 and Executed symbol: ΔΘ5α"
        result = self.executor.execute(expr)
        self.assertEqual(result, expected)

    def test_simple_operation_execution(self):
        expr = "ΔΔ1"
        expected = "Executed symbol: ΔΔ1"
        result = self.executor.execute(expr)
        self.assertEqual(result, expected)

    def test_simple_symbol_execution(self):
        expr = "ΔΔ1"
        expected = "Executed symbol: ΔΔ1"
        result = self.executor.execute(expr)
        self.assertEqual(result, expected)
