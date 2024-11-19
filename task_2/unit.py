import pytest
from unittest.mock import patch
from task_2.solution import save_to_csv
from task_2 import settings


# Mock settings for the test
@pytest.fixture
def mock_settings():
    settings.headers = {"User-Agent": "test-agent"}
    settings.domain = "https://example.com"
    settings.rus_chars = "абвгдеёжзийклмнопрстуфхцчшщэюя"
    settings.start_url = "https://example.com/start"
    settings.BASE_DIR = "/mock/directory"  # Mock file path
    return settings


# Test the save_to_csv function (mocking pandas)
@patch("pandas.DataFrame.to_csv")
def test_save_to_csv(mock_to_csv, mock_settings):
    data = {'А': 1, 'Б': 1, 'В': 1}

    save_to_csv(data)

    mock_to_csv.assert_called_once_with(
        '/mock/directory/beasts.csv', index=False, encoding='utf-8'
    )
