# AIFL Scaling Guide
**Location:** `/docs/orchestrator/scaling.md`

## Deployment Options

### Single Instance
```yaml
resources:
  cpu: 2
  memory: 4Gi
  storage: 20Gi
```

### Multi-Instance
```yaml
deployment:
  replicas: 3
  strategy: RollingUpdate
  load_balancer: round_robin
```

## Resource Guidelines
- 1000 msgs/sec/instance
- 1000 concurrent connections
- 2GB memory baseline
- 1 CPU core baseline

## Performance Tuning
```python
config = {
    "queue_size": 10000,
    "worker_threads": 4,
    "batch_size": 100,
    "timeout_ms": 5000
}
```

## Scaling Triggers
- Queue depth > 1000
- CPU usage > 80%
- Memory usage > 85%
- Response time > 500ms
