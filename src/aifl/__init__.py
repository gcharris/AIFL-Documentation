# src/aifl/__init__.py - Keep this simple with just exports:
from .aifl_parser import AIFLParser
from .aifl_executor import AIFLExecutor
from .encryption import encrypt_data, decrypt_data
from .ai_integrations import OpenAIIntegration, ClaudeIntegration, GeminiIntegration

__all__ = [
    'AIFLParser',
    'AIFLExecutor',
    'encrypt_data',
    'decrypt_data',
    'OpenAIIntegration',
    'ClaudeIntegration',
    'GeminiIntegration'
]