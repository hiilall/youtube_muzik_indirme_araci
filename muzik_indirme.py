from pytube import Playlist
from pytube import YouTube as YT
import threading as th
import time
import os

url="https://www.youtube.com/watch?v=3h3NcrQKtis"

path = os.getcwd()
video=YT(url, use_oauth=True, allow_oauth_cache=True)
strm=video.streams.filter(only_audio=True).first()
print(strm)
strm.download(path)