# tests/unit/test_parser.py
import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from src.aifl.aifl_executor import AIFLExecutor
from src.aifl.aifl_parser import AIFLParser