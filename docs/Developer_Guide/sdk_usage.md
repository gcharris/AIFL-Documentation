# SDK Usage Guide

## Overview
The AIFL SDK provides comprehensive tools and utilities for integrating AI systems with the AIFL framework. This guide covers advanced usage patterns and features of the SDK.

## Core SDK Components

### Client Configuration
```python
from aifl_sdk import AIFLClient, ClientConfig

config = ClientConfig(
    api_key="your_key",
    environment="production",
    timeout=30,
    max_retries=3,
    debug_mode=False,
    metrics_enabled=True
)

client = AIFLClient(config)
```

### Event Handlers
```python
# Message handler
@client.on_message
async def handle_message(message):
    print(f"Received: {message}")

# Connection status handler
@client.on_connection_status
async def handle_status(status):
    print(f"Connection status: {status}")

# Error handler
@client.on_error
async def handle_error(error):
    print(f"Error occurred: {error}")
```

### State Management
```python
# Manage agent state
async def manage_state():
    # Store state
    await client.set_state("processing_status", "active")

    # Retrieve state
    status = await client.get_state("processing_status")

    # Update state
    await client.update_state("processing_status", "completed")
```

## Advanced Message Patterns

### Broadcast Messages
```python
# Send to multiple agents
await client.broadcast(
    message="ΜΑΒ2(Message: 'SystemUpdate')",
    recipients=["agent1", "agent2", "agent3"]
)
```

### Message Streams
```python
# Stream processing
async for message in client.message_stream(filter="data_processing"):
    await process_message(message)
```

### Message Priorities
```python
# Send high-priority message
await client.send_message(
    message="ΜΑΝ1(Topic: 'Emergency')",
    recipient="emergency_handler",
    priority="high"
)
```

## Conversation Management

### Create and Manage Conversations
```python
# Start new conversation
conversation = await client.start_conversation(
    participants=["agent1", "agent2"],
    metadata={
        "topic": "data_analysis",
        "priority": "normal"
    }
)

# Add participant
await conversation.add_participant("agent3")

# Remove participant
await conversation.remove_participant("agent1")

# End conversation
await conversation.end()
```

### Conversation Context
```python
# Set conversation context
await conversation.set_context({
    "domain": "scientific",
    "language": "python",
    "scope": "analysis"
})

# Update context
await conversation.update_context({
    "status": "processing"
})
```

## Error Handling and Recovery

### Retry Patterns
```python
from aifl_sdk.utils import retry_with_backoff

@retry_with_backoff(max_retries=3, initial_delay=1)
async def send_with_retry():
    await client.send_message(message)
```

### Circuit Breaker
```python
from aifl_sdk.utils import circuit_breaker

@circuit_breaker(failure_threshold=5, reset_timeout=60)
async def protected_operation():
    await client.send_message(message)
```

## Middleware and Plugins

### Custom Middleware
```python
from aifl_sdk import Middleware

class LoggingMiddleware(Middleware):
    async def before_send(self, message):
        print(f"Sending message: {message}")
        return message

    async def after_receive(self, message):
        print(f"Received message: {message}")
        return message

# Register middleware
client.add_middleware(LoggingMiddleware())
```

### Plugin System
```python
from aifl_sdk import Plugin

class MetricsPlugin(Plugin):
    def __init__(self):
        self.message_count = 0

    async def on_message_sent(self, message):
        self.message_count += 1

    async def get_metrics(self):
        return {"messages_sent": self.message_count}

# Register plugin
client.register_plugin(MetricsPlugin())
```

## Security Features

### Message Encryption
```python
# Enable end-to-end encryption
client.enable_encryption(
    key_type="RSA",
    key_size=2048
)

# Send encrypted message
await client.send_encrypted_message(
    message="ΣΑΙ1(Topic: 'SecureData')",
    recipient="secure_agent"
)
```

### Authentication
```python
# Token-based authentication
client.set_auth_token("your_token")

# Custom authentication
client.set_auth_handler(custom_auth_handler)
```

## Monitoring and Metrics

### Performance Monitoring
```python
# Enable metrics collection
metrics = client.enable_metrics()

# Get performance data
performance_data = await metrics.get_performance_data()
print(f"Average response time: {performance_data.avg_response_time}ms")
```

### Health Checks
```python
# Check system health
health = await client.check_health()
print(f"System status: {health.status}")
```

## Best Practices

1. **Resource Management**
```python
async with AIFLClient(config) as client:
    # Client automatically handles cleanup
    await client.send_message(message)
```

2. **Batch Processing**
```python
# Process messages in batches
messages = [message1, message2, message3]
await client.send_batch(messages, batch_size=10)
```

3. **Rate Limiting**
```python
# Configure rate limits
client.set_rate_limit(
    max_requests=100,
    per_second=60
)
```

## Testing Utilities

### Mock Client
```python
from aifl_sdk.testing import MockAIFLClient

# Create mock client for testing
mock_client = MockAIFLClient()

# Set up mock responses
mock_client.add_response(
    pattern="ΜΑΝ1",
    response="ΙΑΧ3(Status: 'Success')"
)
```

### Test Helpers
```python
from aifl_sdk.testing import create_test_conversation

# Create test conversation
conversation = await create_test_conversation(
    client,
    num_messages=5
)
```
