# test_api.py
import requests
import json

def test_api():
    base_url = 'http://localhost:8080'  # Updated port to 8080

    # Test health check
    print("Testing health check...")
    response = requests.get(f'{base_url}/health')
    print(f"Health check response: {response.json()}\n")

    # Test AIFL execution
    print("Testing AIFL execution...")
    test_expression = "ΔΕ1(Data: 'TestData', EncryptionType: 'AES256') ∧ ΔΙ5 ⇒ ΔΖ3"
    payload = {
        'expression': test_expression,
        'ai_provider': 'openai'
    }

    try:
        response = requests.post(
            f'{base_url}/execute',
            json=payload,
            headers={'Content-Type': 'application/json'}
        )
        print(f"Execute response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"Error testing execution: {str(e)}")

if __name__ == '__main__':
    test_api()