# Basic Usage

Learn the fundamental concepts and basic usage patterns of AIFL (Artificial Intelligence Function Library).

## Understanding AIFL Symbols

AIFL uses a set of symbols to represent various AI and data processing operations. Here are some key symbols:

- ΔΔ1: Retrieve Data
- ΔΙ5: Normalize Data
- ΔΖ3: Transform Data
- ΔΕ1: Encrypt Data
- ΔΘ5α: Supervised Learning
- ΔΜ1: Train Model
- ΔΝ2: Model Evaluation

For a complete list of symbols, refer to the [Symbol Dictionary](../Core_Concepts/Symbol_Dictionary.md).

## Basic Syntax

AIFL expressions use symbols and operators to describe AI processes. Here are some basic syntax rules:

1. Symbols are combined using operators like ∧ (AND), ∨ (OR), and ⇒ (Implies).
2. Expressions are read from left to right.
3. Parentheses can be used to group operations.

Example:
```
(ΔΔ1 ∧ ΔΙ5) ⇒ ΔΖ3
```
This expression means: Retrieve and normalize data, then transform it.

## Common Usage Patterns

1. Data Processing Pipeline:
   ```
   ΔΔ1 ∧ ΔΙ5 ⇒ ΔΖ3 ⇒ ΔΕ1
   ```
   Retrieve, normalize, transform, and encrypt data.

2. Machine Learning Workflow:
   ```
   (ΔΘ5α ∧ ΔΜ1) ⇒ ΔΝ2
   ```
   Perform supervised learning, train the model, then evaluate it.

3. Error Handling:
   ```
   (ΔΖ3 ∧ ΣΒ2) ⇒ ΦΗ7β
   ```
   If data transformation fails, adjust hyperparameters as a fallback.

## Data Encryption

AIFL now includes robust data encryption using Fernet symmetric encryption. This is represented by the ΔΕ1 symbol:

```python
encrypted_data = encrypt_data(input_data)
encryption_step = f"ΔΕ1('{encrypted_data}')"
```

## Practical Example

Here's a more complex example combining multiple operations:

```python
aifl_process = f"ΔΔ1('{input_data}') ∧ ΔΙ5 ⇒ ΔΖ3 ⇒ ΔΕ1('{encrypted_data}') ∧ (ΔΘ5α ∧ ΔΜ1) ⇒ ΔΝ2"
```

This process:
1. Retrieves and normalizes input data
2. Transforms the data
3. Encrypts the transformed data
4. Performs supervised learning and trains a model
5. Evaluates the trained model

## Next Steps

- Explore the [Syntax Rules](../Core_Concepts/Syntax_Rules.md) for more advanced usage.
- Review [Test Conversations](../Core_Concepts/Test_Conversations.md) for real-world scenarios.
- Practice creating your own AIFL expressions to describe AI processes.
