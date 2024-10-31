# AIFL Message Flow

## Message Lifecycle

### 1. Message Creation
```mermaid
sequenceDiagram
    Agent A->>Orchestrator: send_aifl_message()
    Orchestrator->>Validation: Validate message
    Validation-->>Orchestrator: Validation result
    Orchestrator->>Queue: Queue message
    Queue-->>Orchestrator: Message queued
    Orchestrator-->>Agent A: Message accepted
```

### 2. Message Processing
```mermaid
sequenceDiagram
    Orchestrator->>Queue: Dequeue message
    Orchestrator->>Router: Route message
    Router->>Agent B: Deliver message
    Agent B-->>Router: Acknowledge receipt
    Router-->>Orchestrator: Delivery confirmed
```

## Message States

1. **Submitted**
   - Message received by orchestrator
   - Initial validation performed
   - Assigned message ID

2. **Processing**
   - Message in routing phase
   - Target agents identified
   - Delivery attempted

3. **Delivered**
   - Message received by target
   - Confirmation received
   - History updated

4. **Failed**
   - Delivery unsuccessful
   - Retry if applicable
   - Error reported

## Integration Example

```python
# Sending agent
await orchestrator.send_aifl_message(
    conversation_id="conv_123",
    from_agent="agent_a",
    message="ΜΑΝ1(Topic: 'Example')"
)

# Receiving agent
class MyIntegration(BaseAIIntegration):
    async def send_message(self, aifl_message: str, 
                         conversation_id: str, 
                         context: Dict) -> str:
        response = await self.process_message(aifl_message)
        return response
```

## Error Handling

### Error Types
1. **Validation Errors**: Invalid AIFL syntax
2. **Routing Errors**: Agent not found/available
3. **Delivery Errors**: Communication failures
4. **Protocol Errors**: Invalid message sequence

### Error Response Format
```python
# AIFL error message format
"ΕΧΛ1(ErrorCode: 'CODE', Description: 'details')"
```

## Message Patterns

### 1. Direct Communication
```mermaid
sequenceDiagram
    Agent A->>Orchestrator: Message
    Orchestrator->>Agent B: Message
    Agent B-->>Orchestrator: Response
    Orchestrator-->>Agent A: Response
```

### 2. Broadcast
```mermaid
sequenceDiagram
    Agent A->>Orchestrator: Broadcast
    par Parallel delivery
        Orchestrator->>Agent B: Message
        Orchestrator->>Agent C: Message
        Orchestrator->>Agent D: Message
    end
```

### 3. Sequential Processing
```mermaid
sequenceDiagram
    Agent A->>Orchestrator: Initial message
    Orchestrator->>Agent B: Process step 1
    Agent B-->>Orchestrator: Result 1
    Orchestrator->>Agent C: Process step 2
    Agent C-->>Orchestrator: Final result
```

## Best Practices

1. **Message Design**
   - Use appropriate AIFL symbols
   - Include necessary context
   - Follow protocol specifications

2. **Error Handling**
   - Implement timeout handling
   - Process error responses
   - Follow retry guidelines

3. **Performance**
   - Monitor message sizes
   - Handle responses asynchronously
   - Implement proper cleanup
