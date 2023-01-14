import pytest

from filedpy.services.downloader import youtube_download
from .test_data import (
    TEST_YOUTUBE_LINK,
    TEST_DOWNLOAD_PATH,
    TEST_CLEAN_DOWNLOAD,
)
from filedpy.utils import helpers


@pytest.mark.skip
def test_download_youtube():
    
    result = youtube_download(
        TEST_YOUTUBE_LINK,
        TEST_DOWNLOAD_PATH,
    )

    helpers.clean_up_download(TEST_CLEAN_DOWNLOAD)

    assert result == "Downloaded successfully"
