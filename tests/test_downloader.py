from file_downloader.services.downloader import youtube_download
from .test_data import (
    TEST_YOUTUBE_LINK,
    TEST_DOWNLOAD_PATH,
    TEST_CLEAN_DOWNLOAD,
)
import pytest
from file_downloader import helpers


# @pytest.mark.skip
def test_download_youtube():
    
    result = youtube_download(
        TEST_YOUTUBE_LINK,
        TEST_DOWNLOAD_PATH,
    )
    # TODO: Clean up test download
    helpers.clean_up_download(TEST_CLEAN_DOWNLOAD)

    assert result.get('message') == "Downloaded successfully"
