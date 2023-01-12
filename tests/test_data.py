import os, sys
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
print(BASE)

TEST_YOUTUBE_LINK = 'https://www.youtube.com/watch?v=4TJhBhQk-TY'
TEST_FAKE_YOUTUBE_LINK = 'https://www.twitter'
TEST_DOWNLOAD_PATH = f'{BASE}/tests'
TEST_FAKE_DOWNLOAD_PATH = f'{BASE}/fake_test'