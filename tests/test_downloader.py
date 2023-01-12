from file_downloader.services.downloader import youtube_download
from .test_data import (
    TEST_YOUTUBE_LINK,
    TEST_DOWNLOAD_PATH,
)
import pytest


@pytest.mark.skip
def test_download_youtube():
    
    result = youtube_download(
        TEST_YOUTUBE_LINK,
        TEST_DOWNLOAD_PATH,
    )
    # TODO: Clean up download
    assert result.get('message') == "Downloaded successfully"