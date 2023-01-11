import os, sys
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
print(BASE)

test_youtube_link = 'https://www.youtube.com/watch?v=4TJhBhQk-TY'
test_download_path = f'{BASE}/test'