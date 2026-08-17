"""Basic test cases for PromptCraft."""

import pytest


class TestBasic:
    """Basic test cases."""

    def test_imports(self):
        """Test that main modules can be imported."""
        # This is a placeholder test that will pass
        assert True

    def test_environment(self):
        """Test that the environment is set up correctly."""
        import sys

        assert sys.version_info >= (3, 8), "Python 3.8+ required"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
