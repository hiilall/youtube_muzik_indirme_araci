from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPixmap
import sys
from typing import List
from winreg import SaveKey
from pytube import YouTube
import os
import requests
from bs4 import BeautifulSoup
import urllib.request
import cv2

from pytube import Playlist
from pytube import YouTube as YT
import threading as th

from ui_downloadTool import *


#<yt-formatted-string force-default-style="" class="style-scope ytd-video-primary-info-renderer">Madrigal - Geçme Artık Sokağımdan (Sözleri/Lyrics)</yt-formatted-string>

class AnaPencere(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        
        super(AnaPencere, self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 

        self.ui.pushButtonAra.clicked.connect(self.muzik_ara)
        self.ui.pushButton_indir.clicked.connect(self.muzik_indir)        

    def muzik_ara(self):
        url = self.ui.textEdit_2.toPlainText()
        video=YT(url, use_oauth=True, allow_oauth_cache=True)
        self.ui.labelSarkiAdi.setText(video.title)

        urllib.request.urlretrieve(video.thumbnail_url, 'resim1.jpg')
        img = cv2.imread("resim1.jpg")
        img = cv2.resize(img, (320,240))
        cv2.imwrite("resim1.jpg", img)
        self.pixmap = QPixmap("resim1.jpg")
        self.ui.label_image.setPixmap(self.pixmap)   
        os.remove("resim1.jpg")
     
    def muzik_indir(self):

        """path = os.getcwd()
        tarama=os.scandir(path)
        for belge in tarama:
            if belge.name == "music":
                pass
            else: 
                os.mkdir("music")"""

        url = self.ui.textEdit_2.toPlainText()

        video=YT(url, use_oauth=True, allow_oauth_cache=True)
        strm=video.streams.filter(only_audio=True).first()
        strm.download("C:/Users/hilae/Desktop/music")
        
        """
        sarki_url = "https://www.youtube.com/watch?v=Ah0Ys50CqO8&feature=youtu.be"
        yt = YouTube(sarki_url)
                
        video = yt.streams.filter(only_audio=True).first()

        out_file = video.download()
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        
        # result of success
        print(yt.title + " has been successfully downloaded.")
        
        adres = os.getcwd()
        with os.scandir(adres) as tarama:
            for belge in tarama:
                if belge.name.endswith("mp4"):
                    if belge.name.startswith(yt.title):
                        print("isim",belge.name)
                        #os.remove(belge.name)"""

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create and show mainWindow +icon
    mainWindow = AnaPencere()
    mainWindow.show() 
    sys.exit(app.exec_())