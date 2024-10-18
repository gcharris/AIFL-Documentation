from lark import Lark, Transformer

aifl_grammar = """
    start: expression

    expression: term (OPERATOR term)*

    term: AIFL_SYMBOL
        | aifl_function
        | "(" expression ")"
        | conditional

    conditional: "IF" "(" condition ")" "THEN" expression ("ELSE" expression)?

    condition: expression COMPARISON_OPERATOR (expression | IDENTIFIER)

    aifl_function: AIFL_SYMBOL "(" [arguments] ")"
    arguments: argument ("," argument)*
    argument: key_value | expression | STRING
    key_value: IDENTIFIER ":" (STRING | NUMBER | IDENTIFIER)

    AIFL_SYMBOL: /[ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ][Α-Ωα-ω0-9]*/
    OPERATOR: "∧" | "∨" | "⇒" | "∴" | "¬" | "⊕" | "⊗" | "≡"
    COMPARISON_OPERATOR: ">" | "<" | "==" | ">=" | "<=" | "!="
    STRING: /"[^"]*"/ | /'[^']*'/
    NUMBER: /-?\d+(\.\d+)?/
    IDENTIFIER: /[a-zA-Z_][a-zA-Z0-9_]*/

    %import common.WS
    %ignore WS
"""

class AIFLTransformer(Transformer):
    def start(self, args):
        return args[0]

    def expression(self, args):
        if len(args) == 1:
            return args[0]
        return {"type": "operation", "operator": args[1], "left": args[0], "right": args[2]}

    def term(self, args):
        return args[0]

    def conditional(self, args):
        if len(args) == 3:
            return {"type": "conditional", "condition": args[0], "then": args[1], "else": args[2]}
        return {"type": "conditional", "condition": args[0], "then": args[1]}

    def condition(self, args):
        return {"type": "condition", "left": args[0], "operator": args[1], "right": args[2]}

    def aifl_function(self, args):
        return {"type": "function", "name": args[0], "arguments": args[1] if len(args) > 1 else []}

    def arguments(self, args):
        return args

    def argument(self, args):
        return args[0]

    def key_value(self, args):
        return {"type": "key_value", "key": args[0], "value": args[1]}

    def AIFL_SYMBOL(self, token):
        return {"type": "symbol", "value": token.value}

    def OPERATOR(self, token):
        return token.value

    def COMPARISON_OPERATOR(self, token):
        return token.value

    def STRING(self, token):
        return {"type": "string", "value": token.value[1:-1]}  # Remove quotes

    def NUMBER(self, token):
        return {"type": "number", "value": float(token.value)}

    def IDENTIFIER(self, token):
        return {"type": "identifier", "value": token.value}

class AIFLParser:
    def __init__(self):
        self.parser = Lark(aifl_grammar, parser='lalr', transformer=AIFLTransformer())

    def parse(self, aifl_expression):
        try:
            return self.parser.parse(aifl_expression)
        except Exception as e:
            raise ValueError(f"Failed to parse AIFL expression '{aifl_expression}': {e}")

# Example usage
if __name__ == "__main__":
    parser = AIFLParser()
    test_expressions = [
        "ΔΔ1 ∧ ΔΙ5 ⇒ ΔΖ3",
        "IF(ΔΣ1 > Threshold) THEN ΔΕ1(Data: 'SensitiveInfo') ELSE ΔΑ1(Data: 'PublicInfo')",
        "ΔΕ1(Data: 'UserCredentials', EncryptionType: 'RSA') ∧ (ΔΘ5α ∧ ΔΜ1) ⇒ ΔΝ2",
        "ΔΔ1('Explain the concept of AIFL') ∧ ΔΙ5 ⇒ ΔΖ3"
    ]

    for expr in test_expressions:
        print(f"Parsing: {expr}")
        try:
            result = parser.parse(expr)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")
        print()
