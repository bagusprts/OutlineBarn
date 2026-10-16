# test_outlinebarn.py
"""
Tests for OutlineBarn module.
"""

import unittest
from outlinebarn import OutlineBarn

class TestOutlineBarn(unittest.TestCase):
    """Test cases for OutlineBarn class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OutlineBarn()
        self.assertIsInstance(instance, OutlineBarn)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OutlineBarn()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
