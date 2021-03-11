from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QInputDialog
import sys
from ListView_demo import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.listWidget.addItems(['Kaan','Beyda','Emre'])

        self.ui.btnAdd.clicked.connect(self.addStudent)

    def addStudent(self):

        text, ok = QInputDialog.getText(self, 'new student', 'student add')

        if ok and text is not None:
            self.ui.listWidget.insertItem(0, text)
        else:
            return

def app():
    app = QtWidgets.QApplication(sys.argv)

    win = Window()
    win.show()

    sys.exit(app.exec_())

app()


