# src/aifl_executor.py

from lark import Tree, Token
from src.aifl_parser import AIFLParser

class AIFLExecutor:
    def __init__(self):
        self.parser = AIFLParser()

    def execute(self, expr):
        try:
            tree = self.parser.parse(expr)
            if isinstance(tree, Tree):
                print(f"Parse Tree for '{expr}':\n{tree.pretty()}\n")  # Debugging statement
            else:
                print(f"Parse Tree for '{expr}':\n{tree}\n")  # Token

            return self._execute_tree(tree)
        except Exception as e:
            # Raise exceptions to be handled by the caller (tests)
            print(f"Error executing expression '{expr}': {str(e)}")  # Debugging statement
            raise e

    def _execute_tree(self, tree, indent=0):
        if isinstance(tree, Token):
            # Treat tokens as symbols
            print(f"{'  ' * indent}Processing Token: {tree.value}")  # Debugging statement
            return f"Executed symbol: {tree.value}"
        elif isinstance(tree, Tree):
            print(f"{'  ' * indent}Processing Tree: {tree.data}")  # Debugging statement

            # Handle delegation based on node type
            if tree.data == 'start':
                # Delegate to the child node
                return self._execute_tree(tree.children[0], indent)
            elif tree.data == 'expression':
                # Delegate to the child node
                return self._execute_tree(tree.children[0], indent)
            elif tree.data == 'symbol':
                symbol = tree.children[0].value
                print(f"{'  ' * indent}Executing symbol: {symbol}")  # Debugging statement
                return f"Executed symbol: {symbol}"
            elif tree.data == 'value':
                # Handle value by processing its child token
                print(f"{'  ' * indent}Processing Value")  # Debugging statement
                value_token = tree.children[0]
                if isinstance(value_token, Token):
                    value = self._strip_quotes(value_token.value)
                    print(f"{'  ' * indent}Extracted Value: {value}")  # Debugging statement
                    return value
                else:
                    raise NotImplementedError(f"Unhandled value node child type: {type(value_token)}")
            elif tree.data == 'function_call':
                func_name = tree.children[0].value
                args = {}
                print(f"{'  ' * indent}Executing function: {func_name}")  # Debugging statement

                # Iterate over each argument in the 'arguments' tree
                arguments_tree = tree.children[1] if len(tree.children) > 1 else None
                if arguments_tree:
                    for arg in arguments_tree.children:
                        if isinstance(arg, Tree) and arg.data == 'argument':
                            key_node = arg.children[0]
                            value_node = arg.children[1]

                            # Extract key
                            if isinstance(key_node, Token):
                                key = key_node.value
                            elif isinstance(key_node, Tree):
                                key = self._execute_tree(key_node, indent + 1)
                            else:
                                raise NotImplementedError(f"Unhandled key node type: {type(key_node)}")

                            # Extract value
                            if isinstance(value_node, Token):
                                value = self._strip_quotes(value_node.value)
                            elif isinstance(value_node, Tree):
                                value = self._execute_tree(value_node, indent + 1)
                            else:
                                raise NotImplementedError(f"Unhandled value node type: {type(value_node)}")

                            args[key] = value
                        else:
                            raise ValueError(f"Expected 'argument' tree, got {type(arg)}")
                args_str = ', '.join([f"{k}: {v}" for k, v in args.items()])
                executed_function = f"Executed function: {func_name}({args_str})"
                print(f"{'  ' * indent}{executed_function}")  # Debugging statement
                return executed_function

            # Define operator nodes and expression nodes
            operator_nodes = {'conjunction_op', 'disjunction_op', 'implication_op', 'comparison_op'}
            expression_nodes = {'conjunction', 'disjunction', 'implication', 'comparison'}

            if tree.data in operator_nodes:
                operator_map = {
                    'conjunction_op': '∧',
                    'disjunction_op': '∨',
                    'implication_op': '⇒',
                    'comparison_op': '>'
                }
                operator = operator_map.get(tree.data, tree.data)

                # **Important:** Skip operator tokens and extract operands
                operands = [child for child in tree.children if not isinstance(child, Token)]
                if len(operands) != 2:
                    raise ValueError(f"Operator '{operator}' expected 2 operands, got {len(operands)}")

                print(f"{'  ' * indent}Executing operation: {operator}")  # Debugging statement
                left = self._execute_tree(operands[0], indent + 1)
                right = self._execute_tree(operands[1], indent + 1)

                # Extract symbol names from executed symbols
                left_symbol = left.split(': ')[1] if 'Executed symbol: ' in left else left
                right_symbol = right.split(': ')[1] if 'Executed symbol: ' in right else right

                executed_operation = f"Executed operation: {operator} on Executed symbol: {left_symbol} and Executed symbol: {right_symbol}"
                print(f"{'  ' * indent}{executed_operation}")  # Debugging statement
                return executed_operation

            elif tree.data in expression_nodes:
                # Delegate to the child node (expression)
                return self._execute_tree(tree.children[0], indent)

            elif tree.data == 'conditional':
                print(f"{'  ' * indent}Executing conditional")  # Debugging statement
                condition = self._execute_tree(tree.children[0], indent + 1)
                then_expr = self._execute_tree(tree.children[1], indent + 1)
                else_expr = self._execute_tree(tree.children[2], indent + 1)
                executed_conditional = f"Executed conditional: IF {condition} THEN {then_expr} ELSE {else_expr}"
                print(f"{'  ' * indent}{executed_conditional}")  # Debugging statement
                return executed_conditional

            elif tree.data == 'operand':
                # Handle operand by delegating to its child
                print(f"{'  ' * indent}Processing Operand")  # Debugging statement
                return self._execute_tree(tree.children[0], indent)

            else:
                raise NotImplementedError(f"Unhandled tree data: {tree.data}")
        else:
            raise NotImplementedError(f"Unhandled type: {type(tree)}")

    def _strip_quotes(self, s):
        if isinstance(s, str) and ((s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'"))):
            return s[1:-1]
        return s
