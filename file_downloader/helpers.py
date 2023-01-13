"""
For project helper functions
"""
from pathlib import Path
import os

def check_link(link: str)-> bool:
    # check if link starts with youtube
    if link.startswith('https://www.youtube.com'):
        return True
    return False

def check_path(path: Path) -> bool:
    # check if link starts with youtube
    if os.path.isdir(path):
        return True
    return False

def clean_up_download(path: Path):
    # check path exists
    if os.path.exists(path):
        os.remove(path)
        return True
    return False
