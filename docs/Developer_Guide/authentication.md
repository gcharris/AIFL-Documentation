# Authentication Guide

## Overview
This guide covers authentication and authorization mechanisms in AIFL, ensuring secure communication between agents and platforms.

## API Key Authentication

### Basic Setup
```python
from aifl_sdk import AIFLClient

client = AIFLClient(
    api_key="your_aifl_api_key",
    environment="production"
)
```

### Key Management
```python
# Rotate API key
new_key = await client.rotate_api_key()

# Validate API key
is_valid = await client.validate_api_key()

# Revoke API key
await client.revoke_api_key("old_key_id")
```

## Token-Based Authentication

### JWT Implementation
```python
from aifl_sdk.auth import JWTAuthenticator

# Configure JWT authentication
auth = JWTAuthenticator(
    secret_key="your_secret_key",
    algorithm="HS256"
)

# Create client with JWT auth
client = AIFLClient(
    authenticator=auth,
    environment="production"
)
```

### Token Management
```python
# Generate new token
token = await client.generate_token(
    agent_id="agent_123",
    scopes=["read", "write"]
)

# Validate token
is_valid = await client.validate_token(token)

# Refresh token
new_token = await client.refresh_token(old_token)
```

## OAuth2 Integration

### OAuth2 Setup
```python
from aifl_sdk.auth import OAuth2Config

# Configure OAuth2
oauth_config = OAuth2Config(
    client_id="your_client_id",
    client_secret="your_client_secret",
    redirect_uri="https://your-app/callback",
    scope=["aifl.read", "aifl.write"]
)

# Create client with OAuth2
client = AIFLClient(
    oauth_config=oauth_config,
    environment="production"
)
```

### OAuth2 Flow
```python
# Get authorization URL
auth_url = client.get_authorization_url()

# Exchange code for token
tokens = await client.exchange_code(auth_code)

# Refresh OAuth2 token
new_tokens = await client.refresh_oauth_token(refresh_token)
```

## Multi-Factor Authentication

### MFA Setup
```python
# Enable MFA
mfa_secret = await client.enable_mfa()

# Verify MFA code
await client.verify_mfa_code("123456")

# Disable MFA
await client.disable_mfa(confirmation_code="123456")
```

### Backup Codes
```python
# Generate backup codes
backup_codes = await client.generate_backup_codes()

# Use backup code
await client.use_backup_code("BACKUP-CODE-123")
```

## Role-Based Access Control

### Role Management
```python
# Create role
await client.create_role(
    name="data_analyst",
    permissions=["read_data", "analyze_data"]
)

# Assign role to agent
await client.assign_role(
    agent_id="agent_123",
    role="data_analyst"
)

# Check permissions
has_permission = await client.check_permission(
    agent_id="agent_123",
    permission="read_data"
)
```

### Permission Management
```python
# Create custom permission
await client.create_permission(
    name="custom_action",
    description="Allows custom action"
)

# Grant permission
await client.grant_permission(
    role="data_analyst",
    permission="custom_action"
)
```

## Security Policies

### Password Policies
```python
# Set password policy
client.set_password_policy({
    "min_length": 12,
    "require_special_chars": True,
    "require_numbers": True,
    "max_age_days": 90
})
```

### Session Management
```python
# Configure session policies
client.set_session_policy({
    "max_duration": 3600,  # 1 hour
    "idle_timeout": 900,   # 15 minutes
    "max_concurrent": 3
})

# Terminate session
await client.terminate_session(session_id)
```

## Audit Logging

### Authentication Events
```python
# Enable auth logging
client.enable_auth_logging(
    log_level="INFO",
    include_metadata=True
)

# Get auth logs
auth_logs = await client.get_auth_logs(
    start_time="2024-01-01",
    end_time="2024-01-31"
)
```

### Security Monitoring
```python
# Monitor suspicious activity
client.enable_security_monitoring({
    "failed_attempts": 5,
    "time_window": 300,  # 5 minutes
    "action": "block"
})

# Get security alerts
alerts = await client.get_security_alerts()
```

## Best Practices

### Secure Configuration
```python
# Use environment variables
from dotenv import load_dotenv
import os

load_dotenv()

client = AIFLClient(
    api_key=os.getenv('AIFL_API_KEY'),
    environment=os.getenv('AIFL_ENVIRONMENT')
)
```

### Key Rotation
```python
# Automated key rotation
client.enable_auto_key_rotation(
    interval_days=90,
    notification_email="security@example.com"
)
```

### Rate Limiting
```python
# Configure authentication rate limits
client.set_auth_rate_limits({
    "max_attempts": 5,
    "window_seconds": 300,
    "block_duration": 900
})
```
