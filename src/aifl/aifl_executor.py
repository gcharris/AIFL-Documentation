# src/aifl/aifl_executor.py
import logging
from lark import Tree, Token
from .aifl_parser import AIFLParser  # Changed from src.aifl_parser to relative import

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(message)s')

class AIFLExecutor:
    def __init__(self):
        self.parser = AIFLParser()

    # [Rest of the existing code remains exactly the same]
    def execute(self, expr):
        try:
            tree = self.parser.parse(expr)
            if isinstance(tree, Tree):
                logging.debug(f"Parse Tree for '{expr}':\n{tree.pretty()}\n")
            else:
                logging.debug(f"Parse Tree for '{expr}':\n{tree}\n")

            return self._execute_tree(tree)
        except Exception as e:
            logging.error(f"Error executing expression '{expr}': {str(e)}")
            raise e

    def _execute_tree(self, tree, indent=0):
        indent_str = '  ' * indent
        if isinstance(tree, Token):
            logging.debug(f"{indent_str}Processing Token: {tree.value}")
            return f"Executed symbol: {tree.value}"
        elif isinstance(tree, Tree):
            logging.debug(f"{indent_str}Processing Tree: {tree.data}")

            # Handle delegation based on node type
            if tree.data == 'start':
                return self._execute_tree(tree.children[0], indent)
            elif tree.data == 'expression':
                return self._execute_tree(tree.children[0], indent)
            elif tree.data == 'symbol':
                symbol = tree.children[0].value
                logging.debug(f"{indent_str}Executing symbol: {symbol}")
                return f"Executed symbol: {symbol}"
            elif tree.data == 'value':
                logging.debug(f"{indent_str}Processing Value")
                value_token = tree.children[0]
                if isinstance(value_token, Token):
                    value = self._strip_quotes(value_token.value)
                    logging.debug(f"{indent_str}Extracted Value: {value}")
                    return value
                else:
                    raise NotImplementedError(f"Unhandled value node child type: {type(value_token)}")
            elif tree.data == 'function_call':
                func_name = tree.children[0].value
                args = {}
                logging.debug(f"{indent_str}Executing function: {func_name}")

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
                logging.debug(f"{indent_str}{executed_function}")
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

                # Skip operator tokens and extract operands
                operands = [child for child in tree.children if not isinstance(child, Token)]
                if len(operands) != 2:
                    raise ValueError(f"Operator '{operator}' expected 2 operands, got {len(operands)}")

                logging.debug(f"{indent_str}Executing operation: {operator}")
                left = self._execute_tree(operands[0], indent + 1)
                right = self._execute_tree(operands[1], indent + 1)

                # Check if operands are operations themselves
                if 'Executed operation:' in left:
                    left_str = left
                else:
                    left_str = left  # Could be a symbol or function

                if 'Executed operation:' in right:
                    right_str = right
                else:
                    right_str = right  # Could be a symbol or function

                executed_operation = f"Executed operation: {operator} on {left_str} and {right_str}"
                logging.debug(f"{indent_str}{executed_operation}")
                return executed_operation

            elif tree.data in expression_nodes:
                return self._execute_tree(tree.children[0], indent)

            elif tree.data == 'conditional':
                logging.debug(f"{indent_str}Executing conditional")
                condition = self._execute_tree(tree.children[0], indent + 1)
                then_expr = self._execute_tree(tree.children[1], indent + 1)
                else_expr = self._execute_tree(tree.children[2], indent + 1)
                executed_conditional = f"Executed conditional: IF {condition} THEN {then_expr} ELSE {else_expr}"
                logging.debug(f"{indent_str}{executed_conditional}")
                return executed_conditional

            elif tree.data == 'operand':
                logging.debug(f"{indent_str}Processing Operand")
                return self._execute_tree(tree.children[0], indent)

            else:
                raise NotImplementedError(f"Unhandled tree data: {tree.data}")
        else:
            raise NotImplementedError(f"Unhandled type: {type(tree)}")

    def _strip_quotes(self, s):
        if isinstance(s, str) and ((s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'"))):
            return s[1:-1]
        return s