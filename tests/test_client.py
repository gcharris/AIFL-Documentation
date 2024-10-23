# test_client.py
import requests
import json

def test_api():
    base_url = 'http://localhost:8080'

    # Test health endpoint
    print("Testing health endpoint...")
    response = requests.get(f'{base_url}/health')
    print(json.dumps(response.json(), indent=2))

    # Test execute endpoint
    print("\nTesting execute endpoint...")
    test_expr = "ΔΕ1(Data: 'TestData', EncryptionType: 'AES256') ∧ ΔΙ5 ⇒ ΔΖ3"
    response = requests.post(
        f'{base_url}/execute',
        json={'expression': test_expr}
    )
    print(json.dumps(response.json(), indent=2))

if __name__ == '__main__':
    test_api()