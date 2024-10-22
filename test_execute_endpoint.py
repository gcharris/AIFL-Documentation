import requests
import json
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def test_execute_endpoint():
    url = "http://172.31.196.67:8080/execute"
    headers = {'Content-Type': 'application/json'}
    data = {
        "expression": "IF(ΔΕ1(Data: 'UserCredentials') ∧ (ΔΘ5α ∨ ΔΜ1)) THEN ΔΝ2 ELSE ΔΑ1"
    }

    try:
        logger.info(f"Sending POST request to {url}")
        response = requests.post(url, headers=headers, data=json.dumps(data), timeout=10)
        logger.info(f"Status Code: {response.status_code}")
        logger.debug(f"Response Headers: {response.headers}")
        logger.debug(f"Response Content: {response.text}")
        
        if response.status_code == 200:
            logger.info("Request successful!")
            result = response.json()
            logger.info(f"Execution Result: {result['result']}")
        else:
            logger.error(f"Request failed with status code: {response.status_code}")
            logger.error(f"Error message: {response.text}")
    except requests.exceptions.RequestException as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    test_execute_endpoint()
