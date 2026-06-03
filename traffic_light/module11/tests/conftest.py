import pytest
from unittest.mock import MagicMock


@pytest.fixture
def mock_mqtt_client():
    return MagicMock()