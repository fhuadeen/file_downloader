from file_downloader.services.downloader import youtube_downloader
from .test_data import test_youtube_link, test_download_path


def test_download_youtube():
    
    result = youtube_downloader(
        test_youtube_link,
        test_download_path,
    )
    assert result.get('message') == "Download successful"