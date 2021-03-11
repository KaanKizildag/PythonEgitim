from PyQt5 import QtWidgets
import sys
from PyQt5.QtGui import QIcon
def window():
    # bir pencere oluşturmak için
    app = QtWidgets.QApplication(sys.argv)

    # bir pencere oluşturup bunu gösteriyoruz.
    win = QtWidgets.QMainWindow()
    win.show()

    win.setWindowTitle('İlk Uygulama Başlığı')

    win.setGeometry(200,200, 600, 400) # konumX, konumY, genişlik,
    win.setWindowIcon(QIcon('resim1.jpg')) # ubuntu'da belli olmuyor

    # çarpıya basılınca sistemin durması için
    sys.exit(app.exec_())

window()