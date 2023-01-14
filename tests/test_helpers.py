from filedpy.utils import helpers
from .test_data import (
    TEST_YOUTUBE_LINK,
    TEST_FAKE_YOUTUBE_LINK,
    TEST_DOWNLOAD_PATH,
    TEST_FAKE_DOWNLOAD_PATH,
    TEST_CLEAN_DOWNLOAD,
    TEST_CLEAN_FAKE_DOWNLOAD,
)
import pytest


def test_check_link_true():
    result = helpers.check_link(TEST_YOUTUBE_LINK)
    assert result == True, "Link must be Youtube"

def test_check_link_false():
    result = helpers.check_link(TEST_FAKE_YOUTUBE_LINK)
    assert result == False, "Link must be Youtube"

def test_check_download_path_true():
    result = helpers.check_path(TEST_DOWNLOAD_PATH)
    assert result == True, "Invalid download path"

def test_check_download_path_false():
    result = helpers.check_path(TEST_FAKE_DOWNLOAD_PATH)
    assert result == False, "Invalid download path"

@pytest.mark.skip
def test_clean_up_download_true():
    """Skipped to prevent the test vid from being deleted."""
    result = helpers.clean_up_download(TEST_CLEAN_DOWNLOAD)
    assert result == True, "Invalid path to clean up"

def test_clean_up_download_false():
    result = helpers.clean_up_download(TEST_CLEAN_FAKE_DOWNLOAD)
    assert result == False, "Invalid path to clean up"
