from file_downloader import helpers
from .test_data import (
    TEST_YOUTUBE_LINK,
    TEST_FAKE_YOUTUBE_LINK,
    TEST_DOWNLOAD_PATH,
    TEST_FAKE_DOWNLOAD_PATH,
)


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
