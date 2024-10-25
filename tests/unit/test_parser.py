import pytest
from aifl.aifl_parser import AIFLParser

def test_simple_symbol():
    """Test that we can parse a basic Greek symbol."""
    parser = AIFLParser()
    expression = "ΜΑΝ1"
    result = parser.parse(expression)
    print(f"Test simple_symbol - Result: {result}")
    assert result["type"] == "symbol_call"
    assert result["symbol"] == "ΜΑΝ1"
    assert result["parameters"] == {}

def test_symbol_with_parameters():
    """Test symbol with parameters including an array."""
    parser = AIFLParser()
    expression = "ΜΑΝ1(Agents: [A1], Topic: 'Test')"
    result = parser.parse(expression)
    print(f"Test symbol_with_parameters - Result: {result}")
    assert result["type"] == "symbol_call"
    assert result["symbol"] == "ΜΑΝ1"
    assert result["parameters"]["Agents"] == ["A1"]
    assert result["parameters"]["Topic"] == "Test"

def test_simple_operation():
    """Test basic operation between two symbols."""
    parser = AIFLParser()
    expression = "ΜΑΝ1 ∧ ΜΑΒ2"
    result = parser.parse(expression)
    print(f"Test simple_operation - Result: {result}")
    assert result["type"] == "operation"
    assert result["operator"] == "∧"
    assert result["left"]["type"] == "symbol_call"
    assert result["left"]["symbol"] == "ΜΑΝ1"

def test_not_operation():
    """Test unary NOT operation."""
    parser = AIFLParser()
    expression = "¬ΜΑΝ1"
    result = parser.parse(expression)
    assert result["type"] == "unary_operation"
    assert result["operator"] == "¬"
    assert result["operand"]["type"] == "symbol_call"
    assert result["operand"]["symbol"] == "ΜΑΝ1"

def test_or_operation():
    """Test OR operation."""
    parser = AIFLParser()
    expression = "ΜΑΝ1 ∨ ΜΑΒ2"
    result = parser.parse(expression)
    assert result["type"] == "operation"
    assert result["operator"] == "∨"
    assert result["left"]["type"] == "symbol_call"
    assert result["right"]["type"] == "symbol_call"

def test_implies_operation():
    """Test IMPLIES operation."""
    parser = AIFLParser()
    expression = "ΜΑΝ1 ⇒ ΜΑΒ2"
    result = parser.parse(expression)
    assert result["type"] == "operation"
    assert result["operator"] == "⇒"
    assert result["left"]["type"] == "symbol_call"
    assert result["right"]["type"] == "symbol_call"

def test_operator_precedence():
    """Test operator precedence in a complex expression."""
    parser = AIFLParser()
    expression = "¬ΜΑΝ1 ∧ ΜΑΒ2 ∨ ΜΑΓ3"
    result = parser.parse(expression)
    # The expression should be parsed as ((¬ΜΑΝ1 ∧ ΜΑΒ2) ∨ ΜΑΓ3)
    assert result["type"] == "operation"
    assert result["operator"] == "∨"
    assert result["left"]["type"] == "operation"
    assert result["left"]["operator"] == "∧"
    assert result["left"]["left"]["type"] == "unary_operation"

def test_parentheses():
    """Test explicit grouping with parentheses."""
    parser = AIFLParser()
    expression = "(ΜΑΝ1 ∨ ΜΑΒ2) ∧ ΜΑΓ3"
    result = parser.parse(expression)
    assert result["type"] == "operation"
    assert result["operator"] == "∧"
    assert result["left"]["type"] == "operation"
    assert result["left"]["operator"] == "∨"

def test_symbol_with_greek_suffix():
    """Test symbol with Greek letter suffix."""
    parser = AIFLParser()
    expression = "ΜΑΝ1α"
    result = parser.parse(expression)
    assert result["type"] == "symbol_call"
    assert result["symbol"] == "ΜΑΝ1α"
    assert result["parameters"] == {}