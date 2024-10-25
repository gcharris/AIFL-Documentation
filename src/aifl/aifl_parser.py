from lark import Lark, Transformer
import logging

class AIFLTransformer(Transformer):
    def symbol_call(self, items):
        symbol = str(items[0])
        parameters = items[1] if len(items) > 1 else {}
        return {
            "type": "symbol_call",
            "symbol": symbol,
            "parameters": parameters
        }

    def operation(self, items):
        left, op, right = items
        return {
            "type": "operation",
            "operator": op,
            "left": left,
            "right": right
        }

    def unary_operation(self, items):
        op, operand = items
        return {
            "type": "unary_operation",
            "operator": op,
            "operand": operand
        }

    def parameters(self, items):
        params = {}
        for key, value in items:
            params[str(key)] = value
        return params

    def parameter(self, items):
        key, value = items
        return (str(key), value)

    def value(self, items):
        return items[0]

    def array(self, items):
        return [item for item in items if item is not None]

    # Terminal transformations
    def STRING_LITERAL(self, s): 
        return s[1:-1]  # Remove quotes

    def IDENTIFIER(self, i): 
        return str(i)

    # Operator transformations
    def AND(self, _): return "∧"
    def OR(self, _): return "∨"
    def NOT(self, _): return "¬"
    def IMPLIES(self, _): return "⇒"
    def THEREFORE(self, _): return "∴"
    def COMPOSE(self, _): return "⊗"
    def EQUIV(self, _): return "≡"

class AIFLParser:
    def __init__(self):
        self.logger = logging.getLogger('AIFL.Parser')

        grammar = r"""
        ?start: expression

        ?expression: therefore_expr

        ?therefore_expr: implies_expr
                     | implies_expr THEREFORE therefore_expr -> operation

        ?implies_expr: equiv_expr
                    | equiv_expr IMPLIES implies_expr -> operation

        ?equiv_expr: or_expr
                  | or_expr EQUIV equiv_expr -> operation

        ?or_expr: and_expr
                | or_expr OR and_expr -> operation

        ?and_expr: compose_expr
                | and_expr AND compose_expr -> operation

        ?compose_expr: not_expr
                    | compose_expr COMPOSE not_expr -> operation

        ?not_expr: atom
                | NOT atom -> unary_operation

        ?atom: symbol_call
             | "(" expression ")"

        symbol_call: SYMBOL parameters?
        parameters: "(" parameter ("," parameter)* ")"
        parameter: IDENTIFIER ":" value

        ?value: array
             | STRING_LITERAL
             | IDENTIFIER

        array: "[" [value ("," value)*] "]"

        AND: "∧"
        OR: "∨"
        NOT: "¬"
        IMPLIES: "⇒"
        THEREFORE: "∴"
        COMPOSE: "⊗"
        EQUIV: "≡"

        SYMBOL: /[ΜΙΕΣΔΠΨΩΛΦΡΚΝ][ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ]{0,2}[0-9]+[αβγδε]?/
        IDENTIFIER: /[A-Za-z][A-Za-z0-9_]*/
        STRING_LITERAL: /'[^']*'/ | /"[^"]*"/

        %import common.WS
        %ignore WS
        """

        self.parser = Lark(
            grammar,
            parser='lalr',
            transformer=AIFLTransformer(),
            debug=True
        )

    def parse(self, expression: str) -> dict:
        try:
            self.logger.debug(f"Parsing expression: {expression}")
            result = self.parser.parse(expression)
            self.logger.debug(f"Parse result: {result}")
            return result
        except Exception as e:
            self.logger.error(f"Parse error: {str(e)}")
            raise ValueError(f"Parse error: {str(e)}") from e