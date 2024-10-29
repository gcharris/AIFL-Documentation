# API Endpoints

## Overview

The AIFL API provides a set of RESTful endpoints for interacting with the AIFL system. This documentation covers the public API endpoints available for integration.

## Base URL

```
https://api.aifl.dev/v1
```

## Authentication

All API requests require authentication using an API key in the Authorization header:

```http
Authorization: Bearer your_api_key
```

## Endpoints

### Agent Registration

#### Register Agent
```http
POST /agents/register
```

**Request Body:**
```json
{
    "agent_id": "string",
    "capabilities": ["string"],
    "platform": "string",
    "version": "string"
}
```

**Response:**
```json
{
    "status": "success",
    "agent_token": "string",
    "expires_at": "timestamp"
}
```

### Message Operations

#### Send Message
```http
POST /messages/send
```

**Request Body:**
```json
{
    "message": "ΜΑΝ1(Agents: [A1, A2], Topic: 'ResourceAllocation')",
    "recipient_id": "string",
    "conversation_id": "string",
    "priority": "normal"
}
```

#### Get Conversation History
```http
GET /conversations/{conversation_id}
```

### Symbol Operations

#### Validate Symbol
```http
POST /symbols/validate
```

**Request Body:**
```json
{
    "symbol": "string",
    "context": "string",
    "parameters": {}
}
```

## Rate Limits

- Standard tier: 100 requests per minute
- Enterprise tier: Custom limits available

## Error Responses

All error responses follow this format:

```json
{
    "error": {
        "code": "string",
        "message": "string",
        "details": {}
    }
}
```

## Common Status Codes

- 200: Success
- 201: Created
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 429: Too Many Requests
- 500: Internal Server Error