# AIFL Grammar

AIFL uses a specific grammar to parse and execute expressions. Below are the grammar rules and examples.

## Expression Structure

An expression in AIFL can be:

- **Symbol**: Represents a specific action or function (e.g., `ΔΔ1`).
- **Operation**: Combines symbols using logical operators (e.g., `ΔΔ1 ∧ ΔΙ5`).
- **Function Call**: Invokes a function with arguments (e.g., `ΔΕ1(Data: 'SensitiveInfo')`).
- **Conditional Statement**: Executes functions based on conditions (e.g., `IF(condition) THEN action ELSE alternative`).

## Operators

- **Logical AND (`∧`)**: Combines two expressions where both must be true.
- **Logical OR (`∨`)**: Combines two expressions where at least one must be true.
- **Logical Implication (`⇒`)**: If the preceding expression is true, then the following expression must also be true.

## Functions

Functions perform specific operations and can accept arguments. Example:

- **ΔΕ1(Data: 'SensitiveInfo', EncryptionType: 'AES256')**:
  - **Data**: The data to be encrypted.
  - **EncryptionType**: The type of encryption to use.

## Conditionals

Conditional statements execute different functions based on a condition. Example:

- **IF(ΔΣ1 > Threshold) THEN ΔΕ1(Data: 'SensitiveInfo') ELSE ΔΑ1(Data: 'PublicInfo')**

  - **Condition**: `ΔΣ1 > Threshold`
  - **Then**: Execute `ΔΕ1` with specified data.
  - **Else**: Execute `ΔΑ1` with specified data.

## Examples

1. **Simple Symbol Execution**:
   - **Expression**: `ΔΔ1`
   - **Explanation**: Execute the data retrieval action.

2. **Combined Operations**:
   - **Expression**: `ΔΔ1 ∧ ΔΙ5`
   - **Explanation**: Execute data retrieval AND data integrity check.

3. **Complex Expression**:
   - **Expression**: `ΔΔ1 ∧ ΔΙ5 ⇒ ΔΖ3`
   - **Explanation**: If data retrieval AND integrity check are successful, then perform data zoning.

4. **Function Execution**:
   - **Expression**: `ΔΕ1(Data: 'SensitiveInfo', EncryptionType: 'AES256')`
   - **Explanation**: Encrypt sensitive data using AES256 encryption.
