# test_server.py
import requests
import json

def test_server():
    """Test if the AIFL server is running and responding correctly"""
    base_url = 'http://localhost:3000'

    # Test health endpoint
    try:
        response = requests.get(f'{base_url}/health')
        print("\nHealth check response:", json.dumps(response.json(), indent=2))
    except requests.exceptions.ConnectionError:
        print("\nCould not connect to server. Is it running?")
        return

    # Test execute endpoint
    test_expression = "ΔΕ1(Data: 'TestData') ∧ ΔΙ5"
    try:
        response = requests.post(
            f'{base_url}/execute',
            json={'expression': test_expression}
        )
        print("\nExecute response:", json.dumps(response.json(), indent=2))
    except Exception as e:
        print(f"\nError testing execute endpoint: {str(e)}")

if __name__ == "__main__":
    test_server()