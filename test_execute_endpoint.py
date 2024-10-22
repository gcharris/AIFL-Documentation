import requests
import json
import logging
import time
import statistics

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def test_execute_endpoint(num_tests=10):
    url = "http://172.31.196.67:8080/execute"
    headers = {'Content-Type': 'application/json'}
    data = {
        "message": "IF(ΔΕ1(Data: 'UserCredentials') ∧ (ΔΘ5α ∨ ΔΜ1)) THEN ΔΝ2 ELSE ΔΑ1"
    }

    response_times = []

    for i in range(num_tests):
        try:
            logger.info(f"Sending POST request {i+1}/{num_tests} to {url}")
            start_time = time.time()
            response = requests.post(url, headers=headers, data=json.dumps(data), timeout=10)
            end_time = time.time()
            response_time = end_time - start_time
            response_times.append(response_time)
            
            logger.info(f"Response Time: {response_time:.4f} seconds")
            logger.info(f"Status Code: {response.status_code}")
            
            if response.status_code == 200:
                logger.info("Request successful!")
                result = response.json()
                logger.info(f"Execution Result: {result['result']}")
            else:
                logger.error(f"Request failed with status code: {response.status_code}")
                logger.error(f"Error message: {response.text}")
        except requests.exceptions.RequestException as e:
            logger.error(f"An error occurred: {e}")

    # Calculate statistics
    avg_response_time = statistics.mean(response_times)
    min_response_time = min(response_times)
    max_response_time = max(response_times)
    stddev_response_time = statistics.stdev(response_times) if len(response_times) > 1 else 0

    logger.info(f"Average Response Time: {avg_response_time:.4f} seconds")
    logger.info(f"Minimum Response Time: {min_response_time:.4f} seconds")
    logger.info(f"Maximum Response Time: {max_response_time:.4f} seconds")
    logger.info(f"Standard Deviation: {stddev_response_time:.4f} seconds")

if __name__ == "__main__":
    test_execute_endpoint()
