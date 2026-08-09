import pytest
import asyncio

try:
    import pytest_asyncio  # Check if pytest-asyncio is installed
except ImportError:
    raise ImportError("pytest-asyncio is not installed. Please install it using pip: pip install pytest-asyncio")

async def test_mongodb_connection():
    # ... rest of the function remains the same ...
    # Now the test should run without errors if pytest-asyncio is installed
    pass  # Replace with actual test code

# Add a marker to indicate that this test is an async test
pytestmark = pytest.mark.asyncio  # This line is added to indicate that the test is async
