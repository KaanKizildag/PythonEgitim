from PyQt5 import QtWidgets
import sys
import time

from pytube.exceptions import RegexMatchError
from DownloaderForm import Ui_Form
import threading
from PyQt5.QtWidgets import QMessageBox

from UI.YoutubeDownloader import Downloader


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.btnDownload.clicked.connect(self.INDIR)
        self.ui.tbxUrl.textChanged.connect(self.videoDetaylari)


    def videoDetaylari(self):
        self.ui.tblRes.clear()
        self.ui.tblRes.addItem('Aranıyor')
        try:
            self.ui.tblRes.clear()
            self.ui.tblRes.addItem('Aranıyor')
            threading.Thread(Downloader.analiz(url=self.ui.tbxUrl.text())).start()
            #Downloader.analiz(url=self.ui.tbxUrl.text())
            self.ui.tblRes.clear()
            self.ui.tblRes.addItems(Downloader.liste)
            # print('thread içi islemler')
        except RegexMatchError:
            self.ui.tblRes.clear()
            self.ui.tblRes.addItem('Bulunamadı')

    def INDIR(self):
        index = self.ui.tblRes.currentRow()
        Downloader.download(index=index,url = self.ui.tbxUrl.text())
        print(index)
        QMessageBox.about(self,'indirildi','indirildi')
        print('indirildi')
def App():
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

App()