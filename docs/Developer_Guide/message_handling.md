# Message Handling Guide

## Overview
This guide covers the patterns and best practices for handling AIFL messages in your applications.

## Basic Message Operations

### Sending Messages
```python
# Simple message send
await client.send_message(
    "ΜΑΝ1(Topic: 'DataRequest')",
    recipient_id="target_agent"
)

# Message with context
await client.send_message(
    "ΔΔΦ1(SourceID: 'Database1', Query: 'SELECT *')",
    recipient_id="data_agent",
    context={
        "priority": "high",
        "timeout": 30
    }
)
```

### Receiving Messages
```python
# Message handler
@client.on_message
async def handle_message(message):
    if message.symbol == "ΜΑΝ1":
        await process_negotiation(message)
    elif message.symbol == "ΔΔΦ1":
        await process_data_request(message)

# Start listening
await client.start_receiving()
```

## Advanced Message Patterns

### Broadcast Messages
```python
# Send to multiple recipients
await client.broadcast(
    "ΜΑΒ2(Message: 'SystemUpdate')",
    recipients=["agent1", "agent2", "agent3"]
)

# Send to group
await client.send_to_group(
    "ΜΑΒ2(Message: 'GroupUpdate')",
    group_id="analytics_team"
)
```

### Message Streams
```python
# Create message stream
async with client.message_stream(symbol="ΔΔΦ1") as stream:
    async for message in stream:
        await process_data_message(message)

# Filter stream
async with client.message_stream(
    symbols=["ΜΑΝ1", "ΜΑΒ2"],
    priority="high"
) as stream:
    async for message in stream:
        await process_priority_message(message)
```

## Message Processing

### Message Transformation
```python
# Transform message format
def transform_message(message):
    return {
        "symbol": message.symbol,
        "parameters": message.parameters,
        "context": message.context,
        "metadata": {
            "timestamp": message.timestamp,
            "sender": message.sender_id
        }
    }

# Apply transformation
transformed = transform_message(incoming_message)
```

### Message Validation
```python
# Validate message structure
def validate_message(message):
    required_fields = ["symbol", "parameters"]
    return all(hasattr(message, field) for field in required_fields)

# Validate parameters
def validate_parameters(parameters, schema):
    try:
        validated = schema.validate(parameters)
        return True, validated
    except ValidationError as e:
        return False, str(e)
```

## Message Queuing

### Queue Management
```python
# Configure message queue
client.configure_queue(
    max_size=1000,
    overflow_strategy="drop_oldest"
)

# Add to queue
await client.queue_message(
    "ΜΑΝ1(Topic: 'Queued')",
    recipient_id="agent1"
)

# Process queue
async def process_queue():
    while True:
        message = await client.get_next_message()
        if message:
            await process_message(message)
```

### Priority Queuing
```python
# Set message priority
await client.queue_message(
    "ΜΑΝ1(Topic: 'Urgent')",
    recipient_id="agent1",
    priority="high"
)

# Process by priority
async def process_priority_queue():
    while True:
        message = await client.get_next_priority_message()
        await process_urgent_message(message)
```

## Error Handling

### Message Retry
```python
# Configure retry policy
client.set_retry_policy({
    "max_attempts": 3,
    "initial_delay": 1,
    "max_delay": 10,
    "backoff_factor": 2
})

# Retry handler
@client.on_message_failure
async def handle_failure(message, error):
    if error.is_retryable:
        await client.retry_message(message)
    else:
        await handle_permanent_failure(message, error)
```

### Dead Letter Queue
```python
# Configure DLQ
client.configure_dlq(
    max_size=1000,
    retention_days=7
)

# Move to DLQ
await client.move_to_dlq(
    failed_message,
    reason="Processing failed"
)

# Process DLQ
async def process_dlq():
    async for message in client.get_dlq_messages():
        await reprocess_message(message)
```

## Message Patterns

### Request-Response
```python
# Send request
response = await client.request(
    "ΔΔΦ1(Query: 'GetData')",
    recipient_id="data_service",
    timeout=30
)

# Handle response
if response.status == "success":
    data = response.data
else:
    error = response.error
```

### Pub-Sub
```python
# Subscribe to topic
@client.subscribe("data_updates")
async def handle_updates(message):
    await process_update(message)

# Publish to topic
await client.publish(
    "data_updates",
    "ΔΔΩ2(Update: 'NewData')"
)
```

## Message Monitoring

### Metrics Collection
```python
# Enable message metrics
client.enable_message_metrics({
    "throughput": True,
    "latency": True,
    "error_rate": True
})

# Get metrics
metrics = await client.get_message_metrics(
    timeframe="1h"
)
```

### Message Tracing
```python
# Enable tracing
client.enable_message_tracing(
    sample_rate=0.1
)

# Get trace
trace = await client.get_message_trace(
    message_id="msg_123"
)
```

## Best Practices

### Message Format
```python
# Structured message creation
def create_message(symbol, **parameters):
    return f"{symbol}({', '.join(f'{k}: {v}' for k, v in parameters.items())})"

message = create_message(
    "ΜΑΝ1",
    Topic="DataRequest",
    Priority="high"
)
```

### Performance Optimization
```python
# Batch processing
await client.send_batch(
    messages=[message1, message2, message3],
    batch_size=10
)

# Message compression
client.enable_compression(
    algorithm="gzip",
    threshold=1024  # bytes
)
```

### Logging and Debugging
```python
# Configure message logging
client.configure_message_logging({
    "level": "DEBUG",
    "include_payload": True,
    "max_size": 1024
})

# Debug mode
client.enable_debug_mode(
    trace_messages=True,
    log_level="TRACE"
)
```
