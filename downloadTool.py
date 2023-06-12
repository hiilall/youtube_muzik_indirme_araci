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

        urllib.request.urlretrieve(video.thumbnail_url, 'img.jpg')
        img = cv2.imread("img.jpg")
        img = cv2.resize(img, (320,240))
        cv2.imwrite("img.jpg", img)
        self.pixmap = QPixmap("img.jpg")
        self.ui.label_image.setPixmap(self.pixmap)   
        os.remove("img.jpg")
     
    def muzik_indir(self):

        """path = os.getcwd()
        tarama=os.scandir(path)
        for belge in tarama:
            if belge.name == "music":
                pass
            else: 
                os.mkdir("music")"""

        url = self.ui.textEdit_2.toPlainText()
        adress = os.getcwd()
        if self.ui.radioButtonMp4.isChecked():
            video=YT(url, use_oauth=True, allow_oauth_cache=True)
            stream=video.streams.filter(file_extension='mp4').first()
            stream.download(adress +"/video")
            name = video.title
            with os.scandir(adress+"/video") as tarama:
                for music in tarama:
                    if music.name.startswith(name):
                        self.ui.labelOutput.setText("success")

        else:
            video=YT(url, use_oauth=True, allow_oauth_cache=True)
            strm=video.streams.filter(only_audio=True).first()
            strm.download(adress +"/music")
            name = video.title
            with os.scandir(adress+"/music") as tarama:
                for music in tarama:
                    if music.name.startswith(name):
                        self.ui.labelOutput.setText("success")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create and show mainWindow +icon
    mainWindow = AnaPencere()
    mainWindow.show() 
    sys.exit(app.exec_())