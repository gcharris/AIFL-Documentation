from lark import Lark, Transformer

aifl_grammar = """
    start: expression
    expression: symbol
               | expression OPERATOR expression
               | LPAREN expression RPAREN
               | conditional
               | function_call

    conditional: "IF" LPAREN expression RPAREN "THEN" expression ("ELSE" expression)?
    function_call: symbol LPAREN (argument ("," argument)*)? RPAREN
    argument: expression | ESCAPED_STRING

    symbol: /[ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩαβγδεζηθικλμνξοπρστυφχψω][0-9]*/
    OPERATOR: "∧" | "∨" | "⇒" | "∴" | "¬" | "⊕" | "⊗" | "≡"
    LPAREN: "("
    RPAREN: ")"

    %import common.ESCAPED_STRING
    %import common.WS
    %ignore WS
"""

class AIFLTransformer(Transformer):
    def symbol(self, args):
        return {"type": "symbol", "value": args[0].value}

    def expression(self, args):
        if len(args) == 1:
            return args[0]
        elif len(args) == 3:
            return {"type": "operation", "operator": args[1].value, "left": args[0], "right": args[2]}

    def conditional(self, args):
        if len(args) == 4:
            return {"type": "conditional", "condition": args[0], "then": args[1], "else": args[2]}
        else:
            return {"type": "conditional", "condition": args[0], "then": args[1]}

    def function_call(self, args):
        return {"type": "function_call", "function": args[0], "arguments": args[1:]}

    def argument(self, args):
        return args[0]

    def ESCAPED_STRING(self, s):
        return s[1:-1]

class AIFLParser:
    def __init__(self):
        self.parser = Lark(aifl_grammar, parser='lalr', transformer=AIFLTransformer())

    def parse(self, aifl_expression):
        return self.parser.parse(aifl_expression)

# Example usage
if __name__ == "__main__":
    parser = AIFLParser()
    test_expressions = [
        "ΔΔ1 ∧ ΔΙ5 ⇒ ΔΖ3",
        "IF(ΔΣ1 > Threshold) THEN ΔΕ1(Data: 'SensitiveInfo') ELSE ΔΑ1(Data: 'PublicInfo')",
        "ΔΕ1(Data: 'UserCredentials', EncryptionType: 'RSA')"
    ]

    for expr in test_expressions:
        print(f"Parsing: {expr}")
        result = parser.parse(expr)
        print(f"Result: {result}")
        print()
