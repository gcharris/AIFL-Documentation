# test_server.py
import requests
import json
import time

def test_server():
    """Test basic server functionality"""
    base_url = 'http://localhost:3001'

    print(f"Testing AIFL server at {base_url}")

    try:
        # Test health endpoint
        print("\nTesting health endpoint...")
        response = requests.get(f'{base_url}/health')
        print(json.dumps(response.json(), indent=2))

        # Test simple execution
        print("\nTesting execute endpoint...")
        test_expr = "ΔΕ1(Data: 'TestData') ∧ ΔΙ5"
        response = requests.post(
            f'{base_url}/execute',
            json={'expression': test_expr}
        )
        print(json.dumps(response.json(), indent=2))

    except requests.exceptions.ConnectionError:
        print(f"ERROR: Could not connect to server at {base_url}")
    except Exception as e:
        print(f"Error during test: {str(e)}")

if __name__ == "__main__":
    test_server()