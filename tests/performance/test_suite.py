# test_suite.py
import time
import logging
from statistics import mean, stdev
from typing import Dict, List, Any
from src.aifl import (
    AIFLParser,
    AIFLExecutor,
    OpenAIIntegration,
    ClaudeIntegration,
    GeminiIntegration
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class AIFLTestSuite:
    def __init__(self):
        self.parser = AIFLParser()
        self.executor = AIFLExecutor()

    def get_test_expressions(self) -> List[str]:
        """Get comprehensive set of test expressions"""
        return [
            # Basic operations
            "ΔΕ1(Data: 'TestData', EncryptionType: 'AES256')",
            "ΔΕ1(Data: 'TestData') ∧ ΔΙ5",

            # Nested operations
            "(ΔΕ1(Data: 'TestData') ∧ ΔΙ5) ⇒ ΔΖ3",

            # Conditional expressions
            "IF(ΔΣ1 > Threshold) THEN ΔΕ1(Data: 'SensitiveInfo') ELSE ΔΑ1(Data: 'PublicInfo')",

            # Multiple arguments
            "ΔΕ1(Data: 'TestData', EncryptionType: 'AES256', Priority: 'High')",

            # Complex chains
            "ΔΕ1(Data: 'TestData') ∧ (ΔΙ5 ∨ ΔΖ3) ⇒ ΔΝ2",

            # AI-specific operations
            "ΜΑΝ1(Agents: [A1, A2], Topic: 'ResourceAllocation') ∧ ΜΑΒ2(GroupID: G1)"
        ]

    def get_error_cases(self) -> List[str]:
        """Get test cases for error handling"""
        return [
            # Malformed expressions
            "ΔΕ1(Data: 'Unclosed string)",
            "ΔΕ1(Data:)",
            "ΔΕ1 ∧",

            # Invalid symbols
            "INVALID(Data: 'Test')",
            "ΔΕ1(InvalidParam: 'Test')",

            # Type errors
            "ΔΕ1(Data: 123)",

            # Operator misuse
            "ΔΕ1 ∧ ∧ ΔΙ5",
            "⇒ ΔΕ1"
        ]

    def measure_performance(self, func, test_cases: List[str], iterations: int = 100) -> List[Dict[str, Any]]:
        """Measure execution time and consistency"""
        results = []

        for test_case in test_cases:
            times = []
            for _ in range(iterations):
                start = time.perf_counter()
                try:
                    func(test_case)
                except Exception:
                    continue
                end = time.perf_counter()
                times.append((end - start) * 1000)  # Convert to milliseconds

            if times:  # Only if we had successful executions
                results.append({
                    'test_case': test_case,
                    'avg_time': mean(times),
                    'std_dev': stdev(times) if len(times) > 1 else 0,
                    'min_time': min(times),
                    'max_time': max(times),
                    'success_rate': len(times) / iterations * 100
                })

        return results

    def test_parser_executor(self) -> Dict[str, Any]:
        """Test parsing and execution functionality"""
        results = {
            'passed': 0,
            'failed': 0,
            'details': []
        }

        for expr in self.get_test_expressions():
            try:
                logger.info(f"\nTesting expression: {expr}")
                parsed = self.parser.parse(expr)
                logger.info(f"Parsed result: {parsed}")

                executed = self.executor.execute(expr)
                logger.info(f"Executed result: {executed}")

                results['passed'] += 1
                results['details'].append({
                    'expression': expr,
                    'status': 'passed',
                    'parsed': str(parsed),
                    'executed': str(executed)
                })
            except Exception as e:
                results['failed'] += 1
                results['details'].append({
                    'expression': expr,
                    'status': 'failed',
                    'error': str(e)
                })

        return results

    def test_error_handling(self) -> Dict[str, Any]:
        """Test error handling capabilities"""
        results = {
            'correct_catches': 0,
            'missed_catches': 0,
            'details': []
        }

        for case in self.get_error_cases():
            try:
                self.parser.parse(case)
                results['missed_catches'] += 1
                results['details'].append({
                    'case': case,
                    'status': 'failed to catch error',
                    'error': None
                })
            except Exception as e:
                results['correct_catches'] += 1
                results['details'].append({
                    'case': case,
                    'status': 'successfully caught error',
                    'error': str(e)
                })

        return results

    def run_all_tests(self):
        """Run all tests and generate comprehensive report"""
        logger.info("Starting comprehensive AIFL testing...")

        # Basic functionality tests
        parser_executor_results = self.test_parser_executor()

        # Error handling tests
        error_handling_results = self.test_error_handling()

        # Performance tests
        perf_results = self.measure_performance(
            self.parser.parse,
            self.get_test_expressions(),
            iterations=50
        )

        # Print results
        self._print_test_report(
            parser_executor_results,
            error_handling_results,
            perf_results
        )

    def _print_test_report(self, basic_results, error_results, perf_results):
        """Print formatted test results"""
        print("\n=== AIFL Test Suite Results ===")

        print("\n1. Basic Functionality Tests:")
        print(f"Passed: {basic_results['passed']}")
        print(f"Failed: {basic_results['failed']}")

        print("\n2. Error Handling Tests:")
        print(f"Correct catches: {error_results['correct_catches']}")
        print(f"Missed catches: {error_results['missed_catches']}")

        print("\n3. Performance Results:")
        for result in perf_results:
            print(f"\nExpression: {result['test_case'][:50]}...")
            print(f"Average Time: {result['avg_time']:.2f}ms")
            print(f"Std Deviation: {result['std_dev']:.2f}ms")
            print(f"Success Rate: {result['success_rate']:.1f}%")

if __name__ == "__main__":
    test_suite = AIFLTestSuite()
    test_suite.run_all_tests()