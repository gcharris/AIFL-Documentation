from lark import Lark, Transformer, v_args

@v_args(inline=True)
class AIFLTransformer(Transformer):
    def start(self, expression):
        return expression

    def expression(self, expression):
        return expression

    def implication(self, left, right=None):
        if right is not None:
            return {'type': 'operation', 'operator': '⇒', 'left': left, 'right': right}
        else:
            return left

    def conjunction(self, left, right=None):
        if right is not None:
            return {'type': 'operation', 'operator': '∧', 'left': left, 'right': right}
        else:
            return left

    def term(self, term):
        return term

    def conditional(self, condition, then_expr, else_expr=None):
        result = {'type': 'conditional', 'condition': condition, 'then': then_expr}
        if else_expr is not None:
            result['else'] = else_expr
        return result

    def condition(self, left, op, right):
        return {'type': 'condition', 'left': left, 'operator': op, 'right': right}

    def function_call(self, name, arguments=None):
        if arguments is None:
            arguments = []
        return {'type': 'function', 'name': name['value'], 'arguments': arguments}

    def arguments(self, *args):
        return list(args)

    def key_value_pair(self, key, value):
        return {'type': 'key_value', 'key': key, 'value': value}

    def value(self, value):
        return value

    def AIFL_SYMBOL(self, s):
        return {'type': 'symbol', 'value': str(s)}

    def IDENTIFIER(self, s):
        return {'type': 'identifier', 'value': str(s)}

    def STRING(self, s):
        return {'type': 'string', 'value': s[1:-1]}  # Remove quotes

    def NUMBER(self, n):
        return {'type': 'number', 'value': str(n)}

    def OPERATOR(self, op):
        return str(op)

class AIFLParser:
    def __init__(self):
        self.parser = Lark(r"""
            start: expression

            ?expression: implication

            implication: conjunction "⇒" expression   -> implication
                       | conjunction

            conjunction: conjunction "∧" term          -> conjunction
                       | term

            term: function_call
                | AIFL_SYMBOL
                | IDENTIFIER
                | NUMBER
                | STRING
                | conditional
                | "(" expression ")"

            conditional: "IF" "(" condition ")" "THEN" expression ("ELSE" expression)?

            condition: term OPERATOR term

            OPERATOR: ">" | "<" | ">=" | "<=" | "==" | "!="

            function_call: AIFL_SYMBOL "(" arguments? ")"

            arguments: key_value_pair ("," key_value_pair)*

            key_value_pair: IDENTIFIER ":" value

            value: STRING | NUMBER | IDENTIFIER

            AIFL_SYMBOL: /Δ[Α-Ω]+[0-9]*[α-ω]?/
            IDENTIFIER: /[a-zA-Z_][a-zA-Z0-9_]*/
            STRING: /'[^']*'/
            NUMBER: /\d+(\.\d+)?/

            %import common.WS
            %ignore WS
        """, start='start', parser='lalr', transformer=AIFLTransformer())

    def parse(self, aifl_expression):
        return self.parser.parse(aifl_expression)
