"""from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=d2SNX3bfYKw')

stream = yt.streams.filter(progressive=False, only_video=True).first()

stream.download()

#filter(only_audio=True)# importing packages
"""
from typing import List
from winreg import SaveKey
from pytube import YouTube
import os
  

"""
# url input from user
yt = YouTube(
    str(input("Enter the URL of the video you want to download: \n>> ")))
  
# extract only audio
video = yt.streams.filter(only_audio=True).first()
  
# check for destination to save file
print("Enter the destination (leave blank for current directory)")
destination = str(input(">> ")) or '.'

"""

sarki_listesi = ["https://youtu.be/OpoyWRUlDj0","https://youtu.be/VgqzEPBFuIA","https://youtu.be/SmDKJTXWvV4","https://youtu.be/enuOArEfqGo"
]

"""print(type(sarki_listesi))
print(len(sarki_listesi))"""


while True:
    for i in sarki_listesi:
        yt = YouTube(i)
        
        
        video = yt.streams.filter(only_audio=True).first()


        # download the file
        out_file = video.download()

        
        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        
        # result of success
        print(yt.title + " has been successfully downloaded.")

    

