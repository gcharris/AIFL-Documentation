# src/aifl_parser.py

from lark import Lark

class AIFLParser:
    def __init__(self):
        self.parser = Lark(r"""
            start: expression

            expression: conditional
                       | implication

            conditional: "IF" "(" expression ")" "THEN" expression "ELSE" expression

            implication: disjunction
                        | disjunction IMPLIES implication   -> implication_op

            disjunction: conjunction
                        | conjunction OR disjunction        -> disjunction_op

            conjunction: comparison
                        | comparison AND conjunction          -> conjunction_op

            comparison: operand MORETHAN operand    -> comparison_op
                       | operand

            operand: function_call
                   | symbol
                   | "(" expression ")"

            function_call: IDENTIFIER "(" [arguments] ")"

            arguments: argument ("," argument)*

            argument: IDENTIFIER ":" value

            value: STRING_SINGLE 
                  | STRING_DOUBLE 
                  | IDENTIFIER

            symbol: IDENTIFIER

            STRING_SINGLE : /'[^']*'/
            STRING_DOUBLE : /"[^"]*"/

            # Define operators as tokens
            AND: "∧"
            OR: "∨"
            IMPLIES: "⇒"
            MORETHAN: ">" 

            # Define keywords to prevent them from being treated as IDENTIFIER
            IF: "IF"
            THEN: "THEN"
            ELSE: "ELSE"

            # Updated IDENTIFIER to include both Greek and Latin letters
            IDENTIFIER: /[_\u0391-\u03A9\u03B1-\u03C9A-Za-z][_\u0391-\u03A9\u03B1-\u03C9A-Za-z0-9]*/

            %import common.WS
            %ignore WS
        """, parser='earley', start='start')

    def parse(self, expression):
        return self.parser.parse(expression)
