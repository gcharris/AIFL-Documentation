# tests/test_aifl.py

import unittest
from src.aifl_executor import AIFLExecutor

class TestAIFL(unittest.TestCase):
    def setUp(self):
        self.executor = AIFLExecutor()

    def test_complex_expression(self):
        expr = "ΔΕ1(Data: 'UserCredentials', EncryptionType: 'RSA') ∧ (ΔΘ5α ∧ ΔΜ1) ⇒ ΔΝ2"
        result = self.executor.execute(expr)
        expected = (
            "Executed operation: ⇒ on Executed operation: ∧ on Executed function: ΔΕ1(Data: UserCredentials, EncryptionType: RSA) and Executed operation: ∧ on Executed symbol: ΔΘ5α and Executed symbol: ΔΜ1 and Executed symbol: ΔΝ2"
        )
        self.assertEqual(result.strip(), expected)

    def test_conditional(self):
        expr = "IF(ΔΣ1 > Threshold) THEN ΔΕ1(Data: 'SensitiveInfo') ELSE ΔΑ1(Data: 'PublicInfo')"
        result = self.executor.execute(expr)
        expected = "Executed conditional: IF Executed operation: > on Executed symbol: ΔΣ1 and Executed symbol: Threshold THEN Executed function: ΔΕ1(Data: SensitiveInfo) ELSE Executed function: ΔΑ1(Data: PublicInfo)"
        self.assertEqual(result, expected)

    def test_function_call(self):
        expr = "ΔΕ1(Data: 'SensitiveInfo', EncryptionType: 'AES256')"
        result = self.executor.execute(expr)
        expected = "Executed function: ΔΕ1(Data: SensitiveInfo, EncryptionType: AES256)"
        self.assertEqual(result, expected)

    def test_implication(self):
        expr = "ΔΔ1 ∧ ΔΙ5 ⇒ ΔΖ3"
        result = self.executor.execute(expr)
        expected = "Executed operation: ⇒ on Executed operation: ∧ on Executed symbol: ΔΔ1 and Executed symbol: ΔΙ5 and Executed symbol: ΔΖ3"
        self.assertEqual(result.strip(), expected)

    def test_symbol(self):
        expr = "ΔΔ1"
        result = self.executor.execute(expr)
        expected = "Executed symbol: ΔΔ1"
        self.assertEqual(result.strip(), expected)
