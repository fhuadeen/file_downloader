import os, sys
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
from pathlib import Path

from pytube import YouTube
from pytube.exceptions import VideoUnavailable, RegexMatchError

import filedpy.utils.helpers as helpers


def youtube_download(link: str, download_path: str) -> str:
    """
    For downloading a YouTube video.

    Args:
        - link: str
            The URL of the youtube video.
        - download_path: str
            Path to save the youtube video after downloading it

    Returns: Dict
        - Message stating success of download.
    """

    # check if link is https://www.youtube.com
    check_link = helpers.check_link(link)
    print("Vetting link...")
    if not check_link:
        raise ValueError("Invalid Youtube URL")

    # check if download path exists
    check_download_path = helpers.check_path(Path(download_path))
    print("Vetting download path...")
    if not check_download_path:
        raise ValueError("Invalid download path. Path must be a folder.")
    # try download
    try:
        print("confirming link ID...")
        youtube_obj = YouTube(link)
    except RegexMatchError as e:
        print("Link does not match any Youtube ID:", e)
        return "Can't find video to download"
    youtube_object = youtube_obj.streams.get_highest_resolution()

    # check_vid_availability = youtube_object.check_availability()
    # print(check_vid_availability)
    try:
        print("downloading...")
        youtube_object.download(output_path=download_path)
    except VideoUnavailable as e:
        print("Video unavailable:", e)
        return "Video currently unavailable, please try again later."

    return "Downloaded successfully"

# print(youtube_download(
#     'https://www.youtube.com/watch?v=4TJhBhQk-TY',
#     "/home/fhuad/Downloads/youtube_download"
# ))
