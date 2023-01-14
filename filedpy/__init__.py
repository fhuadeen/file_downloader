"""Package for downloading files."""
# filedpy/__init__.py

__app_name__ = "filedpy"
__version__ = "0.1.0"

(
    SUCCESS,
    URL_ERROR,
    DOWNLOAD_PATH_ERROR,
    YOUTUBE_ID_ERROR,
    DOWNLOAD_ERROR,
) = range(5)

ERRORS = {
    URL_ERROR: "link error",
    DOWNLOAD_PATH_ERROR: "download path error",
    YOUTUBE_ID_ERROR: "youtube id read error",
    DOWNLOAD_ERROR: "video unavailability error",
}
