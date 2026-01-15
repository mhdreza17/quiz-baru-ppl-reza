"""
Root conftest.py - Auto-discovery of all fixtures
"""
import sys
from pathlib import Path

# Add fixtures directory to path
fixtures_dir = Path(__file__).parent / "fixtures"
sys.path.insert(0, str(fixtures_dir))

# Import all fixtures from conftest in fixtures directory
from conftest import *  # noqa: F401, F403
