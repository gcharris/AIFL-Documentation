# AIFL Grammar Reference
**Location:** `/docs/references/grammar.md`

## Overview
This document provides example patterns of AIFL grammar. For complete specification, refer to core documentation.

## Basic Grammar Elements
```ebnf
# Example AIFL Grammar Patterns

?start: expression

?expression: symbol
          | expression operator expression
          | "(" expression ")"
          | asynchronous_expression

symbol: SYMBOL "(" [parameters] ")"
parameters: parameter ("," parameter)*
parameter: KEY ":" VALUE
```

## Common Patterns
```ebnf
# Message Construction
message: symbol parameters
      | message operator message

# Conditional Expressions
conditional: "if" "(" condition ")" "{" expression "}"

# Asynchronous Operations
async_op: expression "↷" "[" context "]"
```

## Example Usage
```python
# Basic message
ΜΑΝ1(Topic: 'Example')

# Combined operations
ΜΑΝ1(Action: 'First') ∧ ΜΑΒ2(Action: 'Second')

# Conditional with context
if (ΣΑ1 == True) { ΜΑΝ1(Topic: 'Proceed') }
```
