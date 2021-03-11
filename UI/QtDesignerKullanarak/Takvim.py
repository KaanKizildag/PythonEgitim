import sys
from PyQt5 import QtWidgets
from dateTime import Ui_MainWindow # tasarımı taşıyan py dosyasından metot çağrılır.

class App(QtWidgets.QMainWindow):
    # yeni bir pencere oluşturuyoruz
    # fakat bir tasarım oluşturmicaz.
    def __init__(self):
        super(App, self).__init__() # QMainWindow 'un ctor u çağrılır.
        self.ui = Ui_MainWindow() # main window içindeki tüm eklenen componentlere
        # bu sayede self.ui.label --> Şeklinde bir erişim sağlanacak
        self.ui.setupUi(self)
        self.ui.btnIslem.clicked.connect(self.BirIslem)

    def BirIslem(self):
        timeEdit = self.ui.dateTimeEdit.dateTime()
        print(timeEdit)
def app():
    app = QtWidgets.QApplication(sys.argv)

    win = App() # burada daha önce QMainWindow veriyorduk
    # fakat tasarım artık App üzerinden gelecek
    # zaten QMainWindow dan kalıtıldı
    win.show()

    sys.exit(app.exec_())

app()