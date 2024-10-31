# AIFL Monitoring Guide
**Location:** `/docs/orchestrator/monitoring.md`

## Health Endpoints
```python
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "version": "1.0.0",
        "connections": 45,
        "queue_depth": 12
    }
```

## Key Metrics
1. Message Processing
   - Queue depth
   - Processing latency
   - Error rates
   - Delivery success

2. System Health
   - Memory usage
   - CPU utilization
   - Network I/O
   - Active connections

## Logging Format
```python
log_entry = {
    "timestamp": "2024-10-30T10:15:30Z",
    "level": "INFO",
    "event": "message_processed",
    "conversation_id": "conv_123",
    "duration_ms": 45
}
```

## Alert Configuration
```yaml
alerts:
  high_latency:
    threshold: 1000ms
    window: 5m
    action: notify

  error_rate:
    threshold: 5%
    window: 15m
    action: page
```
