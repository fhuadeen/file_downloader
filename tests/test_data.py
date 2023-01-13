import os, sys
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
print(BASE)

TEST_YOUTUBE_LINK = 'https://www.youtube.com/watch?v=tPEE9ZwTmy0'
TEST_FAKE_YOUTUBE_LINK = 'https://www.youtube'
TEST_DOWNLOAD_PATH = f'{BASE}/tests'
TEST_FAKE_DOWNLOAD_PATH = f'{BASE}/fake_test'
TEST_CLEAN_DOWNLOAD = f'{BASE}/tests/Shortest Video on Youtube.mp4'
TEST_CLEAN_FAKE_DOWNLOAD = f'{BASE}/fake_test/Shortest Video on Youtube.mp4'