"""
Pytest configuration for test discovery/imports.

Adds project root to Python path so tests can import top-level modules
like `generator.py` and `process.py` in a simple teaching layout.
"""

import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
