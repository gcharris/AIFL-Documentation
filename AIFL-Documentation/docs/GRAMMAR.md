# AIFL Grammar

AIFL (Artificial Intelligence Function Language) uses a specific grammar to parse and execute expressions. This document outlines the grammar rules, syntax, and provides examples to facilitate understanding and implementation.

**Version:** 5.1  
**Last Updated:** September 27, 2024

---

## **Table of Contents**

1. [Expression Structure](#expression-structure)
2. [Grammar Rules](#grammar-rules)
   - [Lexical Elements](#lexical-elements)
   - [Syntax Rules](#syntax-rules)
3. [Operators](#operators)
4. [Functions](#functions)
5. [Conditionals](#conditionals)
6. [Examples](#examples)
7. [Glossary](#glossary)
8. [Additional Recommendations](#additional-recommendations)
9. [Version History](#version-history)

---

## **Expression Structure**

An expression in AIFL can be one of the following:

- **Symbol**: Represents a specific action or function (e.g., `ΔΔ1`).
- **Operation**: Combines symbols using logical operators (e.g., `ΔΔ1 ∧ ΔΙ5`).
- **Function Call**: Invokes a function with arguments (e.g., `ΔΕ1(Data: 'SensitiveInfo')`).
- **Conditional Statement**: Executes functions based on conditions (e.g., `IF(condition) THEN action ELSE alternative`).

---

## **Grammar Rules**

To formally define the structure of AIFL expressions, we use a context-free grammar notation (EBNF - Extended Backus-Naur Form).

### **Lexical Elements**

1. **Identifiers**: Symbols representing actions, functions, or variables.
   - **Format**: Greek letters followed by alphanumeric characters (e.g., `ΔΔ1`, `ΦΑ1`).
   - **Regex**: `[ΔΦΨΛΡΣΕΚΩ][ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ][0-9]*`

2. **Operators**:
   - **Logical AND**: `∧`
   - **Logical OR**: `∨`
   - **Logical Implication**: `⇒`

3. **Parentheses**: `(` and `)` for grouping.

4. **Braces**: `{` and `}` for defining function arguments.

5. **Colon**: `:` used in key-value pairs within function arguments.

6. **Comma**: `,` used to separate multiple arguments.

7. **String Literals**: Enclosed in single quotes `' '` or double quotes `" "` (e.g., `'SensitiveInfo'`).

8. **Numbers**: Integer or decimal numbers (e.g., `0.90`, `1630000000`).

### **Syntax Rules**

```ebnf
<expression>        ::= <conditional> | <operation> | <function_call> | <symbol>

<conditional>       ::= "IF" "(" <condition> ")" "THEN" <expression> "ELSE" <expression>

<condition>         ::= <expression> <comparison_operator> <value>

<comparison_operator>::= ">" | "<" | "==" | "!=" | ">=" | "<="

<operation>         ::= <expression> <logical_operator> <expression>

<logical_operator>  ::= "∧" | "∨" | "⇒"

<function_call>     ::= <symbol> "(" <arguments> ")"

<arguments>         ::= <argument> ("," <argument>)*

<argument>          ::= <key> ":" <value>

<key>               ::= <identifier>

<value>             ::= <string_literal> | <number> | <symbol> | <function_call> | <list>

<list>              ::= "[" <value> ("," <value>)* "]"

<symbol>            ::= <identifier>

<string_literal>    ::= "'" <string_content> "'" | '"' <string_content> '"'

<string_content>    ::= { any character except the enclosing quote }

<number>            ::= <integer> | <decimal>

<integer>           ::= digit+

<decimal>           ::= digit+ "." digit+

<identifier>        ::= letter (letter | digit)*
```



### **Explanation of Rules**

- **Expression**: The most general rule, which can be a conditional statement, an operation, a function call, or a standalone symbol.
- **Conditional**: Represents an `IF-THEN-ELSE` statement, where a condition is evaluated to determine which expression to execute.
- **Condition**: A logical comparison between two expressions or values.
- **Operation**: Combines two expressions using logical operators (`AND`, `OR`, `IMPLICATION`).
- **Function Call**: Invokes a function symbol with a set of arguments.
- **Arguments**: Key-value pairs passed to functions, separated by commas.
- **Value**: Can be a string, number, another symbol, a nested function call, or a list of values.
- **List**: An array of values enclosed in square brackets.

------

## **Operators**

AIFL supports the following logical operators to combine expressions:

- **Logical AND (`∧`)**: Combines two expressions where both must be true.
  - **Example**: `ΔΔ1 ∧ ΔΙ5`
- **Logical OR (`∨`)**: Combines two expressions where at least one must be true.
  - **Example**: `ΔΘ5α ∨ ΔΜ1`
- **Logical Implication (`⇒`)**: If the preceding expression is true, then the following expression must also be true.
  - **Example**: `ΔΔ1 ∧ ΔΙ5 ⇒ ΔΖ3`

### **Operator Precedence and Associativity**

Operators have the following precedence (from highest to lowest):

1. **Parentheses**: `()`
2. **Logical AND**: `∧`
3. **Logical OR**: `∨`
4. **Logical Implication**: `⇒`

*Note: Parentheses can be used to override the default precedence.*

------

## **Functions**

Functions perform specific operations and can accept arguments. The general syntax for a function call is:

```
plaintext
FunctionSymbol(Key1: Value1, Key2: Value2, ...)
```

### **Example:**

```
plaintext
ΔΕ1(Data: 'SensitiveInfo', EncryptionType: 'AES256')
```

- **ΔΕ1**: Function symbol representing data encryption.
- **Data**: The data to be encrypted.
- **EncryptionType**: The type of encryption to use.

### **Rules for Function Calls:**

- **Function Symbol**: Must be a valid identifier as defined in the grammar.
- **Arguments**: Must be provided as key-value pairs.
- **Value Types**: Can include strings, numbers, symbols, nested function calls, or lists.

------

## **Conditionals**

Conditional statements execute different functions based on a condition. The syntax follows the `IF-THEN-ELSE` structure.

### **Syntax:**

```
plaintext
IF(condition) THEN action ELSE alternative
```

### **Components:**

- **Condition**: A logical comparison that evaluates to true or false.
- **Then**: The expression to execute if the condition is true.
- **Else**: The expression to execute if the condition is false.

### **Example:**

```
plaintext
IF(ΔΣ1 > Threshold) THEN ΔΕ1(Data: 'SensitiveInfo') ELSE ΔΑ1(Data: 'PublicInfo')
```

- **Condition**: `ΔΣ1 > Threshold`
- **Then**: Execute `ΔΕ1` with specified data.
- **Else**: Execute `ΔΑ1` with specified data.

------

## **Examples**

### **1. Simple Symbol Execution**

- **Expression**: `ΔΔ1`
- **Explanation**: Execute the data retrieval action.

### **2. Combined Operations**

- **Expression**: `ΔΔ1 ∧ ΔΙ5`
- **Explanation**: Execute data retrieval AND data integrity check.

### **3. Complex Expression**

- **Expression**: `ΔΔ1 ∧ ΔΙ5 ⇒ ΔΖ3`
- **Explanation**: If data retrieval AND integrity check are successful, then perform data zoning.

### **4. Function Execution**

- **Expression**: `ΔΕ1(Data: 'SensitiveInfo', EncryptionType: 'AES256')`
- **Explanation**: Encrypt sensitive data using AES256 encryption.

### **5. Conditional Statement**

- **Expression**: `IF(ΔΣ1 > Threshold) THEN ΔΕ1(Data: 'SensitiveInfo') ELSE ΔΑ1(Data: 'PublicInfo')`
- **Explanation**: If the value of `ΔΣ1` is greater than `Threshold`, execute the encryption function; otherwise, execute the data access function.

### **6. Nested Functions and Operations**

- **Expression**: `ΔΕ1(Data: ΔΔ1(ΣDT100), EncryptionType: 'RSA') ∧ (ΔΘ5α ∨ ΔΜ1)`
- **Explanation**: Encrypt data retrieved from `ΣDT100` using RSA encryption AND initiate supervised learning OR train the model.

### **7. Complex Conditional with Nested Operations**

- **Expression**: `IF(ΔΣ1 > Threshold ∧ ΔΜ1) THEN ΔΕ1(Data: 'SensitiveInfo') ELSE (ΔΑ1(Data: 'PublicInfo') ∨ ΔΞ3)`
- **Explanation**: If `ΔΣ1` is greater than `Threshold` AND `ΔΜ1` is true, execute `ΔΕ1`; otherwise, execute `ΔΑ1` OR `ΔΞ3`.

### **8. List as Function Argument**

- **Expression**: `ΡΣΥ3(Action: 'SynchronizeSensorData', Sensors: [Lidar, Camera], Participants: [ExplorerIDAlpha, ExplorerIDBeta], Timestamp: 1630000500)`
- **Explanation**: Synchronize sensor data for specified sensors and participants at a given timestamp.

------

## **Glossary**

For quick reference, here's an alphabetical list of all symbols used in AIFL:

- **CompatibilityCheck**: Verify Compatibility
- **ΔΔ1**: Retrieve Data
- **ΔΔ2**: Restore Data Integrity
- **ΔΙ5**: Normalize Data
- **ΔΖ3**: Transform Data
- **ΔΘ5α**: Supervised Learning
- **ΔΘ5β**: Unsupervised Learning
- **ΔΗ1**: Hyperparameter Adjustment
- **ΔΜ1**: Train Model
- **ΔΝ2**: Model Evaluation
- **ΔΞ3**: Update Model Parameters
- **ΕΑ2**: Actuator Error
- **ΕΔΛ1**: Learning Update
- **ΕΠΡ1**: Error Propagation
- **ΕΣ1**: Sensor Error
- **IncompatibilityError**: Incompatibility Error
- **ΚΝS1**: Knowledge Share
- **ΛΑ1**: Model Accuracy
- **ΛΑ2**: Anomaly Detection Metrics
- **ΛΗ1**: Mean Absolute Percentage Error (MAPE)
- **ΛΚ1**: Number of Clusters
- **ΛΜ2**: Mean Squared Error (MSE)
- **ΛΘ2**: Sharpe Ratio
- **ΛΣ2**: Cluster Details
- **ΦΑ1**: Start Process
- **ΦΑR1**: Activate Recovery
- **ΦΚ1**: Risk Assessment Measures
- **ΦΗ7β**: Adjust Hyperparameters
- **ΦΗ7δ**: Apply Fallback Mechanism
- **ΦΗ7ε1**: Adjust Investment Strategy
- **ΦΖ6**: Abort Operation
- **ΡΧ1**: Real-Time Command
- **ΡΧ1Ε**: Emergency Stop
- **ΡΧ1Ο**: Collision Avoidance
- **ΡΧ1Π**: Prioritized Interrupt
- **ΡΣΥ3**: Synchronize
- **ΣΑ1**: Success State
- **ΣΓ3**: Progress Update
- **ΨΑ1**: Detect Security Breach
- **ΨΛ1**: Initiate Secure Session
- **ΨΣ1**: Trigger Security Alert
- **ΨΔ2**: Identify Breach Source
- **ΨΕ3**: Execute Security Protocol
- **ΨΓ3**: Provide Progress Update
- **ΨΙ9**: Initiate Data Validation
- **ΨΙ10**: Complete Data Integrity Restoration
- **ValidateData**: Data Integrity Validation

