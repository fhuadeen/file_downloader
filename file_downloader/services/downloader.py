import os, sys
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
from pytube import YouTube
import helpers
from pathlib import Path


def youtube_download(link: str, download_path: str) -> dict:

    # check if link is https://www.youtube.com
    check_link = helpers.check_link(link)
    if not check_link:
        raise ValueError("Invalid Youtube URL")

    # check if download path exists
    check_download_path = helpers.check_path(Path(download_path))
    if not check_download_path:
        raise ValueError("Invalid download path")
    # try download
    youtube_obj = YouTube(link)
    youtube_object = youtube_obj.streams.get_highest_resolution()

    # check_vid_availability = youtube_object.check_availability()
    # print(check_vid_availability)
    try:
        youtube_object.download()
    except Exception as e:
        raise "An error occurred while downloading"

    return {
        "success": True,
        "message": "Downloaded successfully"
    }

# print(youtube_download(
#     'https://www.youtube.com/watch?v=4TJhBhQk-TY',
#     BASE
# ))
# print(f"{BASE}")