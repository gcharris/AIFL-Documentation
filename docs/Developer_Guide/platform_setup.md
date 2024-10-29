# Platform Setup Guide

## Overview
This guide covers the setup and configuration of AIFL with various AI platforms and frameworks.

## Environment Setup

### 1. Development Environment
```python
# .env configuration
AIFL_API_KEY=your_aifl_api_key
AIFL_ENVIRONMENT=development
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
GEMINI_API_KEY=your_gemini_key
```

```python
# Load environment variables
from dotenv import load_dotenv
import os

load_dotenv()

# Configure AIFL client
from aifl_sdk import AIFLClient

client = AIFLClient(
    api_key=os.getenv('AIFL_API_KEY'),
    environment=os.getenv('AIFL_ENVIRONMENT')
)
```

## Platform-Specific Setup

### OpenAI Integration

```python
from aifl_sdk.platforms import OpenAIConfig

# Configure OpenAI settings
openai_config = OpenAIConfig(
    api_key=os.getenv('OPENAI_API_KEY'),
    model="gpt-4",
    temperature=0.7,
    max_tokens=1000
)

# Register with AIFL client
client.register_platform(openai_config)
```

### Anthropic Claude Integration

```python
from aifl_sdk.platforms import ClaudeConfig

# Configure Claude settings
claude_config = ClaudeConfig(
    api_key=os.getenv('ANTHROPIC_API_KEY'),
    model="claude-3-sonnet",
    temperature=0.7
)

# Register with AIFL client
client.register_platform(claude_config)
```

### Google Gemini Integration

```python
from aifl_sdk.platforms import GeminiConfig

# Configure Gemini settings
gemini_config = GeminiConfig(
    api_key=os.getenv('GEMINI_API_KEY'),
    model="gemini-pro",
    temperature=0.7
)

# Register with AIFL client
client.register_platform(gemini_config)
```

## Platform Capabilities

### Capability Registration
```python
# Register platform capabilities
client.register_capabilities({
    "text_generation": ["openai", "claude", "gemini"],
    "code_generation": ["openai", "claude"],
    "image_analysis": ["gemini"],
    "data_analysis": ["all"]
})
```

### Platform-Specific Features
```python
# OpenAI function calling
await client.invoke_function(
    platform="openai",
    function_name="analyze_data",
    parameters={"data_type": "numeric"}
)

# Claude XML mode
await client.set_platform_mode(
    platform="claude",
    mode="xml",
    enabled=True
)

# Gemini safety settings
await client.configure_safety(
    platform="gemini",
    settings={
        "harassment": "block_medium_and_above",
        "hate_speech": "block_medium_and_above"
    }
)
```

## Multi-Platform Configuration

### Load Balancing
```python
# Configure platform priorities
client.set_platform_priorities({
    "openai": 1,    # Primary
    "claude": 2,    # Secondary
    "gemini": 3     # Tertiary
})

# Enable automatic failover
client.enable_failover(
    retry_attempts=3,
    failover_delay=1.0
)
```

### Cost Management
```python
# Set platform budgets
client.set_platform_budgets({
    "openai": {
        "daily_limit": 100.0,
        "warning_threshold": 80.0
    },
    "claude": {
        "daily_limit": 50.0,
        "warning_threshold": 40.0
    }
})
```

## Security Configuration

### API Key Management
```python
# Rotate platform API keys
await client.rotate_platform_key(
    platform="openai",
    new_key="new_api_key"
)

# Validate platform credentials
status = await client.validate_platform_credentials()
```

### Access Controls
```python
# Set platform access rules
client.set_platform_access({
    "openai": ["team_a", "team_b"],
    "claude": ["team_a"],
    "gemini": ["team_b"]
})
```

## Monitoring and Logging

### Platform Metrics
```python
# Enable platform monitoring
client.enable_platform_monitoring({
    "request_logging": True,
    "performance_metrics": True,
    "cost_tracking": True
})

# Get platform statistics
stats = await client.get_platform_stats(
    platform="openai",
    timeframe="24h"
)
```

### Health Checks
```python
# Check platform health
health = await client.check_platform_health()
for platform, status in health.items():
    print(f"{platform}: {status}")

# Set up health alerts
client.configure_health_alerts(
    email="admin@example.com",
    slack_webhook="https://hooks.slack.com/..."
)
```

## Testing Configuration

### Platform Mocks
```python
from aifl_sdk.testing import PlatformMock

# Create platform mock
mock = PlatformMock(platform="openai")
mock.add_response(
    prompt="Hello",
    response="Hi there!"
)

# Use mock in tests
client.use_mock(mock)
```

### Integration Tests
```python
# Test platform integration
async def test_platform_integration():
    result = await client.test_platform(
        platform="openai",
        test_type="basic",
        timeout=30
    )
    assert result.status == "passed"
```

## Troubleshooting

### Common Issues
1. API Key Issues
```python
# Verify API keys
await client.verify_platform_keys()
```

2. Rate Limiting
```python
# Check rate limits
limits = await client.get_rate_limits()
```

3. Connection Issues
```python
# Test platform connectivity
connectivity = await client.test_connectivity()
```

### Platform Status
```python
# Get platform status
status = await client.get_platform_status()
print(f"OpenAI Status: {status.openai}")
print(f"Claude Status: {status.claude}")
print(f"Gemini Status: {status.gemini}")
```
