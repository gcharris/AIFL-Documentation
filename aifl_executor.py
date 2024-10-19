import logging
from aifl_parser import AIFLParser

class AIFLExecutor:
    def __init__(self):
        self.parser = AIFLParser()
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.ERROR)

    def execute(self, aifl_expression):
        try:
            parsed_expression = self.parser.parse(aifl_expression)
            print(f"Parsed Expression: {parsed_expression}")  # Debug Statement
            result = self._execute_node(parsed_expression)
            print(f"Result type before conversion: {type(result)}")  # Debug Statement
            result_str = str(result)
            print(f"Result after conversion to string: {result_str}")  # Debug Statement
            return result_str
        except Exception as e:
            self.logger.error(f"Error executing AIFL expression: {e}")
            return f"Error: {str(e)}"

    def _execute_node(self, node, indent=0):
        if isinstance(node, dict):
            node_type = node.get('type', '').lower()  # Ensure lowercase
            print(f"Processing node_type: {node_type}")  # Debug Statement
            if node_type == 'symbol':
                return f"Executed symbol: {node['value']}"
            elif node_type == 'operation':
                return self._execute_operation(node, indent)
            elif node_type == 'function':
                return self._execute_function(node)
            elif node_type == 'conditional':
                return self._execute_conditional(node)
            elif node_type == 'condition':
                return self._execute_condition(node)
            elif node_type in ['string', 'identifier', 'number']:
                return node['value']
            else:
                print(f"Unhandled node type: {node_type}")  # Debug Statement
                return str(node)
        elif isinstance(node, list):
            # If node is a list, process each item and join with commas
            processed_nodes = [self._execute_node(n, indent) for n in node]
            return ', '.join(processed_nodes)
        else:
            # If node is neither dict nor list, convert it to string
            return str(node)

    def _execute_operation(self, node, indent=0):
        operator = node['operator']
        left_result = self._execute_node(node['left'], indent + 2)
        right_result = self._execute_node(node['right'], indent + 2)
        indent_str = ' ' * indent
        print(f"Executing operation: {operator}")  # Debug Statement
        return f"{indent_str}Executed operation: {operator}\n{indent_str}  Left: {left_result}\n{indent_str}  Right: {right_result}"

    def _execute_function(self, node):
        function_name = node['name']
        arguments = [self._format_argument(arg) for arg in node.get('arguments', [])]
        print(f"Executing function: {function_name} with arguments: {arguments}")  # Debug Statement
        return f"Executed function: {function_name}({', '.join(arguments)})"

    def _format_argument(self, arg):
        if isinstance(arg, dict) and arg['type'] == 'key_value':
            key = arg['key']['value']
            # Ensure 'value' is a string, not a dict
            if isinstance(arg['value'], dict) and 'value' in arg['value']:
                value = arg['value']['value']
            else:
                value = str(arg['value'])
            print(f"Formatting argument: {key} = {value}")  # Debug Statement
            return f"{key}: {value}"
        else:
            return str(arg)

    def _execute_conditional(self, node):
        condition_result = self._execute_node(node['condition'])
        then_result = self._execute_node(node['then'])
        else_result = self._execute_node(node['else']) if 'else' in node else None
        print(f"Executing conditional with condition: {condition_result}, then: {then_result}, else: {else_result}")  # Debug Statement
        result = f"Executed conditional:\n  Condition: {condition_result}\n  Then: {then_result}"
        if else_result:
            result += f"\n  Else: {else_result}"
        return result

    def _execute_condition(self, node):
        left = self._execute_node(node['left'])
        operator = node['operator']
        right = self._execute_node(node['right'])
        print(f"Executing condition: {left} {operator} {right}")  # Debug Statement
        return f"{left} {operator} {right}"

if __name__ == "__main__":
    executor = AIFLExecutor()
    test_expressions = [
        "ΔΔ1",
        "ΔΔ1 ∧ ΔΙ5",
        "ΔΔ1 ∧ ΔΙ5 ⇒ ΔΖ3",
        "ΔΕ1(Data: 'SensitiveInfo', EncryptionType: 'AES256')",
        "IF(ΔΣ1 > Threshold) THEN ΔΕ1(Data: 'SensitiveInfo') ELSE ΔΑ1(Data: 'PublicInfo')",
        "ΔΕ1(Data: 'UserCredentials', EncryptionType: 'RSA') ∧ (ΔΘ5α ∧ ΔΜ1) ⇒ ΔΝ2"
    ]

    for expr in test_expressions:
        print(f"Testing expression: {expr}")
        result = executor.execute(expr)
        print(f"Result: {result}\n")
