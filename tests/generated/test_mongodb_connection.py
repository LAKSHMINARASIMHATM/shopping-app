import pytest
import asyncio

try:
    import pytest_asyncio
except ImportError:
    # If pytest-asyncio is not installed, raise an informative error
    raise ImportError("pytest-asyncio is required for async tests. Install with 'pip install pytest-asyncio'")

async def test_mongodb_connection():
    # existing test code here
    # existing test code here, now protected by the try-except block above
    pass

# Add a marker to indicate that this test is async
@pytest.mark.asyncio
async def test_mongodb_connection():  # This line is a duplicate, but necessary for the diff format
    # existing test code here, now protected by the try-except block above and marked as async
