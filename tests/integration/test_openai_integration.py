import pytest
from aifl.ai_integrations.openai_integration import OpenAIIntegration
import os

def test_openai_integration_initialization():
    """Test that OpenAIIntegration initializes correctly with API key."""
    integration = OpenAIIntegration()
    assert integration is not None
    assert integration.api_key is not None
    assert len(integration.api_key) > 0

def test_simple_symbol_processing():
    """Test processing of a simple symbol call."""
    integration = OpenAIIntegration()

    # Create a simple symbol call result
    executed_result = {
        "type": "symbol_call",
        "symbol": "ΜΑΝ1",
        "parameters": {
            "Agents": ["A1", "A2"],
            "Topic": "ResourceAllocation"
        }
    }

    result = integration.process(executed_result)
    print(f"OpenAI processing result: {result}")

    assert result["status"] == "success"
    assert "result" in result
    assert "model" in result
    assert result["model"] == "gpt-3.5-turbo"
    assert isinstance(result["result"], str)
    assert len(result["result"]) > 0