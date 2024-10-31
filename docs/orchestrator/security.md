# AIFL Security Guide
**Location:** `/docs/orchestrator/security.md`

## Authentication
```python
# Agent authentication
auth_config = {
    "api_key": "your_secret_key",
    "cert_path": "/path/to/cert",
    "auth_type": "bearer"
}

integration = MyPlatformIntegration(auth_config)
await orchestrator.register_agent("agent_id", integration)
```

## Rate Limiting
- Default: 100 requests/minute per agent
- Burst: 150 requests/minute maximum
- Cooldown: 60 seconds after burst

## Access Control
```python
# Permission levels
permissions = {
    "conversation_create": True,
    "message_send": True,
    "participant_add": False
}

# Role assignment
await orchestrator.set_agent_permissions("agent_id", permissions)
```

## Message Security
- TLS 1.3+ for transport
- Message signing required
- Payload encryption optional
- Max message size: 1MB

## Best Practices
1. Rotate keys monthly
2. Monitor access patterns
3. Log security events
4. Regular security audits
