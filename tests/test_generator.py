import random
from typing import List, Dict, Optional

class AIFLTestGenerator:
    def __init__(self):
        self.symbols = {
            'ΜΑ': ['ΜΑΝ1', 'ΜΑΒ2', 'ΜΑΗ3', 'ΜΑΛ4', 'ΜΑΥ5'],
            'ΙΑ': ['ΙΑΣ1', 'ΙΑΠ2', 'ΙΑΧ3', 'ΙΑΤ4', 'ΙΑΛ5'],
            'ΣΑ': ['ΣΑΙ1', 'ΣΑΚ2', 'ΣΑΜ3', 'ΣΑΡ4', 'ΣΑΒ5']
        }
        self.operators = ['∧', '∨', '⇒', '∴', '¬', '⊕', '⊗', '≡', '↷']

    def generate_parameters(self, symbol: str) -> Dict[str, str]:
        """Generate appropriate parameters for a given symbol."""
        param_templates = {
            'ΜΑΝ1': {'Agents': '[A{}, A{}]', 'Topic': '"{}"'},
            'ΣΑΙ1': {'AgentID': 'A{}', 'SessionID': 'S{}'},
            'ΙΑΣ1': {'Topic': '"{}"', 'AgentID': 'A{}'}
        }

        if symbol in param_templates:
            params = {}
            for key, template in param_templates[symbol].items():
                if '{}' in template:
                    if '[' in template:  # List of agents
                        params[key] = template.format(
                            random.randint(1, 10),
                            random.randint(1, 10)
                        )
                    else:  # Single value
                        params[key] = template.format(random.randint(1, 100))
                else:
                    params[key] = template
            return params
        return {}

    def generate_expression(self, depth: int = 0, max_depth: int = 3) -> str:
        """Generate a random AIFL expression with nested operations."""
        if depth >= max_depth or random.random() < 0.3:
            # Generate a single symbol with parameters
            prefix = random.choice(list(self.symbols.keys()))
            symbol = random.choice(self.symbols[prefix])
            params = self.generate_parameters(symbol)
            param_str = ', '.join(f'{k}: {v}' for k, v in params.items())
            return f"{symbol}({param_str})"

        # Generate a compound expression
        left = self.generate_expression(depth + 1, max_depth)
        operator = random.choice(self.operators)
        right = self.generate_expression(depth + 1, max_depth)

        return f"({left} {operator} {right})"

    def generate_test_conversation(self, num_exchanges: int = 3) -> List[Dict[str, str]]:
        """Generate a complete test conversation between AI agents."""
        conversation = []
        for _ in range(num_exchanges):
            exchange = {
                'sender': f'Agent{random.randint(1,5)}',
                'receiver': f'Agent{random.randint(1,5)}',
                'message': self.generate_expression(),
                'timestamp': f'2024-10-23T{random.randint(0,23):02d}:{random.randint(0,59):02d}:{random.randint(0,59):02d}Z'
            }
            conversation.append(exchange)
        return conversation

    def validate_expression(self, expression: str) -> bool:
        """Validate that an AIFL expression follows correct syntax."""
        # Basic validation rules - could be expanded
        try:
            # Check balanced parentheses
            if expression.count('(') != expression.count(')'):
                return False

            # Check for valid symbols
            symbols = set()
            for prefix in self.symbols:
                symbols.update(self.symbols[prefix])

            # Simple tokenization and validation
            tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()
            for token in tokens:
                if (token not in symbols and 
                    token not in self.operators and 
                    token not in ['(', ')'] and
                    not token.startswith('{') and
                    not token.endswith('}') and
                    not ':' in token):
                    return False

            return True
        except Exception:
            return False

# Example usage
if __name__ == "__main__":
    generator = AIFLTestGenerator()

    # Generate a single expression
    print("Single Expression:")
    expression = generator.generate_expression()
    print(expression)
    print(f"Valid: {generator.validate_expression(expression)}\n")

    # Generate a test conversation
    print("Test Conversation:")
    conversation = generator.generate_test_conversation(3)
    for exchange in conversation:
        print(f"From: {exchange['sender']}")
        print(f"To: {exchange['receiver']}")
        print(f"Time: {exchange['timestamp']}")
        print(f"Message: {exchange['message']}")
        print()