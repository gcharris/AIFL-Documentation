# test_quick.py
from src.aifl import AIFLParser, AIFLExecutor, OpenAIIntegration

def test_basic_functionality():
    print("Testing AIFL basic functionality...")

    # Test Parser
    print("\n1. Testing Parser:")
    parser = AIFLParser()
    test_expr = "ΔΕ1(Data: 'TestData', EncryptionType: 'AES256') ∧ ΔΙ5 ⇒ ΔΖ3"
    try:
        result = parser.parse(test_expr)
        print(f"✓ Parser test passed")
        print(f"Parsed result: {result}")
    except Exception as e:
        print(f"✗ Parser test failed: {str(e)}")

    # Test Executor
    print("\n2. Testing Executor:")
    executor = AIFLExecutor()
    try:
        result = executor.execute(test_expr)
        print(f"✓ Executor test passed")
        print(f"Executed result: {result}")
    except Exception as e:
        print(f"✗ Executor test failed: {str(e)}")

    # Test OpenAI Integration
    print("\n3. Testing OpenAI Integration:")
    openai = OpenAIIntegration()
    try:
        result = openai.process("Test input")
        print(f"✓ OpenAI integration test passed")
        print(f"OpenAI result: {result}")
    except Exception as e:
        print(f"✗ OpenAI integration test failed: {str(e)}")

if __name__ == "__main__":
    test_basic_functionality()