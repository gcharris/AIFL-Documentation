# src/aifl/aifl_executor.py
import logging
from .aifl_parser import AIFLParser

class AIFLExecutor:
    def __init__(self):
        self.parser = AIFLParser()
        self.logger = logging.getLogger('AIFL.Executor')

    def execute(self, expr: str) -> str:
        """Execute an AIFL expression."""
        try:
            ast = self.parser.parse(expr)
            return self._execute_ast(ast)
        except Exception as e:
            self.logger.error(f"Execution error: {str(e)}")
            raise

    def _execute_ast(self, ast: dict) -> str:
        """Execute an AST node."""
        if isinstance(ast, dict):
            if ast.get('type') == 'symbol_call':
                return f"Executed symbol: {ast['symbol']}"
            elif ast.get('type') == 'operation':
                left = self._execute_ast(ast['left'])
                right = self._execute_ast(ast['right'])
                return f"Executed operation: {ast['operator']} on {left} and {right}"
        return str(ast)