# AIFL Integration Guide

## Quick Start

```python
from aifl.orchestrator import AIFLOrchestrator
from aifl.integrations import BaseAIIntegration

class MyPlatformIntegration(BaseAIIntegration):
    async def send_message(
        self, 
        aifl_message: str,
        conversation_id: str,
        context: Dict
    ) -> str:
        # Process AIFL message
        result = await self.platform_api.process(aifl_message)
        # Return AIFL response
        return f"ΜΑΒ2(Result: '{result}')"

# Initialize and register
orchestrator = AIFLOrchestrator()
await orchestrator.register_agent(
    "my_agent",
    MyPlatformIntegration()
)
```

## Integration Requirements

1. **BaseAIIntegration Implementation**
   - Implement send_message method
   - Handle AIFL message parsing
   - Generate AIFL responses
   - Manage platform context

2. **Error Handling**
   - Catch platform errors
   - Convert to AIFL errors
   - Implement retry logic
   - Log error details

3. **Connection Management**
   - Maintain platform connection
   - Handle authentication
   - Monitor health status
   - Cleanup resources

## Testing Integration

```python
async def test_integration():
    integration = MyPlatformIntegration()
    
    # Test message handling
    response = await integration.send_message(
        "ΜΑΝ1(Topic: 'Test')",
        "test_conv",
        {}
    )
    
    # Verify AIFL response
    assert response.startswith("ΜΑΒ2")
```

## Platform-Specific Guidelines

### OpenAI Integration
```python
class OpenAIIntegration(BaseAIIntegration):
    def __init__(self):
        self.client = AsyncOpenAI()
        
    async def send_message(self, ...):
        response = await self.client.chat.completions.create(...)
        return self._to_aifl(response)
```

### Claude Integration
```python
class ClaudeIntegration(BaseAIIntegration):
    def __init__(self):
        self.client = AsyncAnthropicAPI()
        
    async def send_message(self, ...):
        response = await self.client.complete(...)
        return self._to_aifl(response)
```

### Gemini Integration
```python
class GeminiIntegration(BaseAIIntegration):
    def __init__(self):
        self.client = AsyncGeminiAPI()
        
    async def send_message(self, ...):
        response = await self.client.generate_content(...)
        return self._to_aifl(response)
```
