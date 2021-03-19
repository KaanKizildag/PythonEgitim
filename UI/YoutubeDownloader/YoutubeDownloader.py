from PyQt5 import QtWidgets
import sys
from DownloaderForm import Ui_Form
from Downloader import download

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.tblRes.addItems(['144p','360p','480p'])
        #self.ui.btnDownload.clicked.connect(download)

def App():
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())

App()

