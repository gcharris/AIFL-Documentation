# AIFL Syntax Rules and Conventions

This document outlines the syntax rules for using AIFL (Artificial Intelligence Function Library) effectively.

## Formal Grammar (EBNF)

```
<expression> ::= <symbol>
               | <expression> <operator> <expression>
               | <asynchronous_expression>
               | <conditional_expression>
               | <error_propagation>
               | <ros_namespace>
               | <ros_node_handle>
               | <data_structure_expression>
               | '(' <expression> ')'

<asynchronous_expression> ::= <expression> '↷' '[' <context> ']'

<conditional_expression> ::= 'if' '(' <condition> ')' '{' <expression> '}'

<error_propagation> ::= 'ΕΠΡ1' '('
                          'SourceError' ':' <error_instance> ','
                          'Recipient' ':' <recipient_list> ','
                          'DetailLevel' ':' <detail_level> ','
                          'Timestamp' ':' <timestamp>
                       ')'

<ros_namespace> ::= 'ΣROSN1' '(' 'Namespace' ':' <namespace> ')' '{' <ros_expression> '}'

<ros_node_handle> ::= 'ΣROSNH2' '(' 'NodeName' ':' <node_name> ')' '{' <ros_expression> '}'

<ros_expression> ::= <ros_publish> | <ros_service_call> | <ros_action_send_goal>

<data_structure_expression> ::= 'Error' '{' <error_properties> '}' 
                               | 'ModelUpdate' '{' <model_properties> '}'
                               | 'NonTextData' '{' <data_properties> '}'

<symbol>     ::= 'ΦΑ1' | 'ΔΔ1' | 'ΔΙ5' | 'ΔΖ3' | 'ΔΘ5α' | 'ΔΜ1' | 'ΔΝ2' | 'ΛΑ1' | 'ΛΜ2' | 'ΛΗ1' | 'ΛΘ2' | 'ΛΚ1' | 'ΛΣ2' | 'ΛΑ2' | 'ΦΚ1' | 'ΦΗ7ε1' | 'ΦΗ7β' | 'ΦΗ7δ' | 'ΦΖ6' | 'ΨΑ1' | 'ΨΛ1' | 'ΨΣ1' | 'ΨΔ2' | 'ΨΕ3' | 'ΨΙ9' | 'ΨΙ10' | 'ΨΓ3' | 'ΩΑ1' | 'ΩΒ2' | 'ΣΑ1' | 'ΣΓ3' | 'ΡΧ1' | 'ΡΧ1Ε' | 'ΡΧ1Ο' | 'ΡΧ1Π' | 'ΡΣΥ3' | 'ΕΔΛ1' | 'ΚΝS1' | 'CompatibilityCheck' | 'ValidateData' | 'ΕΠΡ1' | 'ΣROSN1' | 'ΣROSNH2' | 'ΔΕ1' | ...

<operator>   ::= '∧'    (* Logical AND *)
               | '∨'    (* Logical OR *)
               | '⇒'    (* Implies *)
               | '∴'    (* Therefore *)
               | '¬'    (* Not *)
               | '⊕'    (* Exclusive OR *)
               | '⊗'    (* Operation *)
               | '≡'    (* Equivalent to *)
               | '↷'    (* Asynchronous Interrupt *)

<condition> ::= <expression> <comparison_operator> <expression>

<comparison_operator> ::= '==' | '!=' | '<' | '>' | '<=' | '>='

<statement>  ::= <expression>
               | <statement> ';' <statement>

<property> ::= <identifier>

<value> ::= <string> | <number> | <array> | <object>

<namespace> ::= <string>

<node_name> ::= <string>

<dependency> ::= <identifier> 'v' <version_number>

<version_number> ::= <number> '.' <number> [ '.' <number> ]

<identifier> ::= [A-Za-z_][A-Za-z0-9_]*

<string> ::= '"' .*? '"'

<number> ::= [0-9]+ ('.' [0-9]+)?
```

## Operator Precedence and Associativity

**Operator Precedence (from highest to lowest):**

1. Parentheses `( )`
2. Not `¬`
3. Operation `⊗`
4. Asynchronous Interrupt `↷`
5. And `∧`
6. Or `∨`
7. Exclusive OR `⊕`
8. Implies `⇒`, Equivalent `≡`
9. Therefore `∴`

**Associativity:**

- **Left-associative:** `∧`, `∨`, `⊕`, `⊗`
- **Right-associative:** `⇒`, `≡`, `∴`, `↷`

## Example Expressions

### Example 1: Machine Learning Workflow

```
((ΔΘ5α ∧ ΔΜ1) ⇒ ΔΝ2) ∴ ΣΑ1
```

*Interpretation:* If supervised learning and model training are performed, then model evaluation follows; therefore, success state is achieved.

### Example 2: Error Handling with Fallback

```
((ΔΖ3 ∧ ΣΒ2) ⇒ ΦΗ7β)
```

*Interpretation:* If data transformation results in a failure state, then adjust hyperparameters as a fallback mechanism.

### Example 3: Secure Communication Initiation

```
(ΩΑ1 ∧ ΨΛ1(ΣID123) ∧ ΨΑ1) ⇒ (ΨΣ1 ∧ ΨΔ2) ⇒ (ΨΕ3 ∧ ΦΖ6)
```

*Interpretation:* Initiate communication, start a secure session with ID `ΣID123`, detect a security breach, trigger a security alert, identify the breach source, and execute abort operation.

### Example 4: Real-Time Interrupt with Context Preservation

```
ΡΧ1Ε(PriorityLevel: Critical) ↷ [CurrentTask]
```

*Interpretation:* The emergency stop command interrupts the current task asynchronously, preserving the task's context for potential resumption.

### Example 5: Hierarchical Error Handling with Conditional Recovery

```
Error{
    Type: ΕΑ2,
    ComponentID: MotorActuator05,
    ErrorType: Overheating,
    SeverityLevel: Warning
} ⇒
if (SeverityLevel == Critical) {
    Execute ΦΑR1(Procedure: ShutdownActuator)
} else if (SeverityLevel == Warning) {
    Execute ΦΑR1(Procedure: ReduceActuatorLoad)
}
```

*Interpretation:* Depending on the severity level, execute the appropriate recovery procedure.

### Example 6: Data Encryption

```
ΔΕ1(Data: "SensitiveInfo", EncryptionType: "AES256") ⇒ ΨΙ9
```

*Interpretation:* Encrypt the sensitive information using AES256 encryption, then initiate data validation to ensure integrity.

## Usage Guidelines

1. **Consistency:** Use symbols consistently to maintain clarity.
2. **Modularity:** Leverage modular constructs for related operations.
3. **Validation:** Always validate data and compatibility before proceeding.
4. **Error Handling:** Utilize hierarchical error handling and propagation.
5. **Documentation:** Maintain comprehensive documentation for all symbols and constructs.

## Best Practices

1. **Clear Communication:** Use precise symbols and structured expressions.
2. **Redundancy Avoidance:** Avoid redundant expressions by using modular constructs.
3. **Scalability:** Design expressions with scalability in mind.
4. **Security Considerations:** Incorporate security and privacy symbols to ensure compliance.
5. **Continuous Refinement:** Regularly review and refine symbols and syntax.
