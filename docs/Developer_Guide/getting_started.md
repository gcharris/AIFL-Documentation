# Getting Started with AIFL

## Overview

AIFL (AI Foundational Language) is a framework that enables standardized communication between AI systems. This guide will help you get started with implementing AIFL in your applications.

## Prerequisites

- Python 3.8 or higher
- pip package manager
- Basic understanding of async programming
- API keys for your AI platforms (if using specific integrations)

## Installation

### 1. Install AIFL SDK
```bash
pip install aifl-sdk
```

### 2. Install Platform Dependencies
```bash
# For OpenAI integration
pip install openai

# For Google Gemini integration
pip install google-generativeai

# For Anthropic Claude integration
pip install anthropic
```

## Quick Start

### 1. Basic Setup
```python
from aifl_sdk import AIFLClient

# Initialize AIFL client
client = AIFLClient(
    api_key="your_aifl_api_key",
    environment="production"  # or "development" for testing
)
```

### 2. Register Your Agent
```python
# Register your application as an AIFL agent
agent_id = await client.register_agent(
    name="MyAIApplication",
    capabilities=["text_processing", "data_analysis"],
    description="My AI application using AIFL"
)
```

### 3. Send Your First Message
```python
# Send a simple AIFL message
response = await client.send_message(
    "ΜΑΝ1(Topic: 'Greeting')",
    recipient_id="target_agent",
    conversation_id="conv_123"
)

print(f"Response received: {response}")
```

## Basic Concepts

### 1. Messages
AIFL messages use a standardized format with symbols and parameters:
```python
# Resource allocation request
"ΜΑΝ1(Agents: [A1, A2], Topic: 'ResourceAllocation')"

# Data processing request
"ΔΔΦ1(SourceID: 'Database1', Query: 'SELECT *')"
```

### 2. Conversations
AIFL maintains conversation context:
```python
# Start a conversation
conversation = await client.start_conversation(
    participants=["agent1", "agent2"],
    metadata={
        "domain": "data_processing",
        "priority": "normal"
    }
)

# Send message in conversation context
await client.send_message(
    "ΙΑΣ1(Topic: 'DataAnalysis')",
    conversation_id=conversation.id
)
```

### 3. Error Handling
```python
from aifl_sdk.exceptions import AIFLError

try:
    response = await client.send_message(message, recipient_id)
except AIFLError as e:
    print(f"AIFL error occurred: {e}")
    # Handle error appropriately
```

## Configuration

### 1. Environment Setup
```python
# Development environment
client = AIFLClient(
    api_key="your_key",
    environment="development",
    debug=True
)

# Production environment
client = AIFLClient(
    api_key="your_key",
    environment="production",
    timeout=30,
    retry_attempts=3
)
```

### 2. Logging Configuration
```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('aifl_sdk')
```

## Next Steps

1. Review the [Symbol Dictionary](../Core_Concepts/symbol-dictionary.md) to understand available AIFL symbols
2. Learn about [Message Handling](message_handling.md) for more advanced messaging patterns
3. Explore [Platform Setup](platform_setup.md) for platform-specific configurations
4. Check [Best Practices](best_practices.md) for optimization and security guidelines

## Common Issues and Solutions

### 1. Authentication Issues
```python
# Ensure your API key is properly set
client = AIFLClient(
    api_key=os.getenv('AIFL_API_KEY'),  # Use environment variables
    environment="production"
)
```

### 2. Connection Timeouts
```python
# Configure longer timeouts for slow connections
client = AIFLClient(
    api_key="your_key",
    timeout=60,  # 60 seconds
    retry_attempts=5
)
```

### 3. Rate Limiting
```python
# Handle rate limiting with exponential backoff
from aifl_sdk.utils import exponential_backoff

@exponential_backoff(max_retries=3)
async def send_with_retry(client, message):
    return await client.send_message(message)
```

## Example Applications

### 1. Simple Chat Agent
```python
async def chat_agent():
    client = AIFLClient(api_key="your_key")

    # Register agent
    agent_id = await client.register_agent(
        name="ChatAgent",
        capabilities=["chat"]
    )

    # Handle incoming messages
    @client.on_message
    async def handle_message(message):
        if message.type == "chat":
            response = await process_chat(message)
            await client.send_message(response, message.sender)

    await client.start()
```

### 2. Data Processing Agent
```python
async def data_processor():
    client = AIFLClient(api_key="your_key")

    # Register data processing agent
    agent_id = await client.register_agent(
        name="DataProcessor",
        capabilities=["data_analysis"]
    )

    # Handle data processing requests
    @client.on_message
    async def handle_request(message):
        if message.symbol == "ΔΔΦ1":
            result = await process_data(message.parameters)
            response = f"ΔΔΑ4(DataSetID: '{result.id}', Status: 'Processed')"
            await client.send_message(response, message.sender)

    await client.start()
```

## Support and Resources

- [AIFL Documentation](https://docs.aifl.dev)
- [API Reference](../api-reference/endpoints.md)
- [Community Forums](https://community.aifl.dev)
- [GitHub Repository](https://github.com/aifl/aifl-sdk)

