from aifl_parser import AIFLParser
from aifl_executor import AIFLExecutor

def test_parser_and_executor():
    parser = AIFLParser()
    executor = AIFLExecutor()
    expressions = [
        "ΔΔ1",
        "ΔΔ1 ∧ ΔΙ5",
        "ΔΔ1 ∧ ΔΙ5 ⇒ ΔΖ3",
        "ΔΕ1(Data: 'SensitiveInfo', EncryptionType: 'AES256')",
        "IF(ΔΣ1 > Threshold) THEN ΔΕ1(Data: 'SensitiveInfo') ELSE ΔΑ1(Data: 'PublicInfo')",
        "ΔΕ1(Data: 'UserCredentials', EncryptionType: 'RSA') ∧ (ΔΘ5α ∧ ΔΜ1) ⇒ ΔΝ2"
    ]
    
    for expr in expressions:
        print(f"\nTesting expression: {expr}")
        try:
            parsed = parser.parse(expr)
            print("Parsing successful!")
            print("Parsed result:", parsed)
            
            executed = executor.execute(parsed)
            print("Execution successful!")
            print("Execution result:", executed)
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_parser_and_executor()
