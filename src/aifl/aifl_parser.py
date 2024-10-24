# src/aifl/aifl_parser.py enhancement
from lark import Lark, Transformer, v_args
import logging

class AIFLParser:
    def __init__(self):
        self.logger = logging.getLogger('AIFL.Parser')
        self.parser = Lark(r"""
            ?start: expression

            expression: conditional
                     | asynchronous
                     | operation
                     | symbol_call
                     | "(" expression ")"

            conditional: "IF" "(" condition ")" "THEN" expression "ELSE" expression
            asynchronous: expression "↷" "[" expression "]"
            operation: expression operator expression

            symbol_call: SYMBOL ("(" [parameters] ")")?
            parameters: parameter ("," parameter)*
            parameter: IDENTIFIER ":" value

            value: STRING_LITERAL 
                | NUMBER
                | BOOLEAN
                | array
                | IDENTIFIER

            array: "[" [value ("," value)*] "]"

            operator: "∧" -> and_op
                   | "∨" -> or_op
                   | "⇒" -> implies_op
                   | "∴" -> therefore_op
                   | "¬" -> not_op
                   | "⊕" -> xor_op
                   | "⊗" -> compose_op
                   | "≡" -> equiv_op

            condition: expression comparison_operator expression
            comparison_operator: "==" | "!=" | "<" | ">" | "<=" | ">="

            SYMBOL: /[ΜΙΕΣΔΠΨΩΛΦΡΚΝ][ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ]?[0-9]+[αβγδε]?/

            IDENTIFIER: /[A-Za-z_][A-Za-z0-9_]*/
            STRING_LITERAL: /"[^"]*"/ | /'[^']*'/
            NUMBER: /-?\d+(\.\d+)?/
            BOOLEAN: "True" | "False"

            %import common.WS
            %ignore WS
        """, parser='earley', start='start')

    def parse(self, expression: str) -> dict:
        """Parse an AIFL expression into an AST."""
        try:
            self.logger.debug(f"Parsing expression: {expression}")
            tree = self.parser.parse(expression)
            return self._transform_tree(tree)
        except Exception as e:
            self.logger.error(f"Parse error in expression '{expression}': {str(e)}")
            raise

    def _transform_tree(self, tree):
        """Transform parse tree into a structured format."""
        if isinstance(tree, str):
            return {"type": "literal", "value": tree}

        data = tree.data if hasattr(tree, 'data') else None
        children = tree.children if hasattr(tree, 'children') else []

        if data == 'symbol_call':
            return {
                "type": "symbol_call",
                "symbol": str(children[0]),
                "parameters": self._transform_tree(children[1]) if len(children) > 1 else {}
            }
        elif data == 'operation':
            return {
                "type": "operation",
                "operator": self._transform_tree(children[1]),
                "left": self._transform_tree(children[0]),
                "right": self._transform_tree(children[2])
            }
        # Add more transformation cases...

        return tree