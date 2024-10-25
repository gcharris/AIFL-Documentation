import pytest
from aifl import AIFLExecutor

def test_simple_symbol_execution():
    """Test that we can execute a basic symbol."""
    executor = AIFLExecutor()
    expression = "ΜΑΝ1"
    result = executor.execute(expression)
    print(f"Test simple_symbol_execution - Result: {result}")
    assert "Executed symbol: ΜΑΝ1" in result

def test_symbol_with_parameters_execution():
    """Test execution of symbol with parameters."""
    executor = AIFLExecutor()
    expression = "ΜΑΝ1(Agents: [A1], Topic: 'Test')"
    result = executor.execute(expression)
    print(f"Test symbol_with_parameters_execution - Result: {result}")
    assert "Executed symbol: ΜΑΝ1" in result

def test_simple_operation_execution():
    """Test execution of an operation between two symbols."""
    executor = AIFLExecutor()
    expression = "ΜΑΝ1 ∧ ΜΑΒ2"
    result = executor.execute(expression)
    print(f"Test simple_operation_execution - Result: {result}")
    assert "Executed operation: ∧" in result
    assert "ΜΑΝ1" in result
    assert "ΜΑΒ2" in result

def test_complex_operation_execution():
    """Test execution of a complex operation with multiple operators."""
    executor = AIFLExecutor()
    expression = "(ΜΑΝ1 ∨ ΜΑΒ2) ∧ ΜΑΓ3"
    result = executor.execute(expression)
    print(f"Test complex_operation_execution - Result: {result}")
    assert "Executed operation: ∧" in result
    assert "Executed operation: ∨" in result
    assert "ΜΑΝ1" in result
    assert "ΜΑΒ2" in result
    assert "ΜΑΓ3" in result

def test_error_handling():
    """Test that executor properly handles invalid expressions."""
    executor = AIFLExecutor()
    with pytest.raises(Exception):
        executor.execute("invalid expression")

def test_nested_operations():
    """Test execution of deeply nested operations."""
    executor = AIFLExecutor()
    expression = "ΜΑΝ1 ∧ (ΜΑΒ2 ∨ (ΜΑΓ3 ∧ ΜΑΔ4))"
    result = executor.execute(expression)
    print(f"Test nested_operations - Result: {result}")
    assert "Executed operation: ∧" in result
    assert "Executed operation: ∨" in result
    assert all(symbol in result for symbol in ["ΜΑΝ1", "ΜΑΒ2", "ΜΑΓ3", "ΜΑΔ4"])