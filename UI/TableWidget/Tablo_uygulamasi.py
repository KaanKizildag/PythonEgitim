from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import sys
from table_form import Ui_MainWindow

class Window(QtWidgets.QMainWindow):

    def __init__(self):

        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # bu bilgiler veri tabanı gibi başka yerlerden de çekildiği varsayılsın.
        self.products = [
            {'name': 'Lenovo', 'price': 4000},
            {'name': 'Asus', 'price': 5000},
            {'name': 'Dell', 'price': 3000},
            {'name': 'Monster', 'price': 3000},
            {'name': 'Dell', 'price': 7000},
            {'name': 'Hp', 'price': 8000}
        ]


        self.loadItems()
        self.ui.btnSave.clicked.connect(self.saveItem)


    def saveItem(self):
        name = self.ui.tbxName.text()
        price = self.ui.tbxPrice.text()
        if name and price is not None:
            self.products.append(
                {'name': name , 'price': price}
            )
            self.loadItems()

    def loadItems(self):

        self.ui.tblProducts.setRowCount(len(self.products))
        self.ui.tblProducts.setColumnCount(2)
        self.ui.tblProducts.setHorizontalHeaderLabels(['Name', 'Price'])

        row = 0
        for product in self.products:
            self.ui.tblProducts.setItem(row, 0, QTableWidgetItem(product['name']))
            self.ui.tblProducts.setItem(row, 1, QTableWidgetItem(str(product['price'])))
            row += 1
        '''

        self.ui.tblProducts.setRowCount(3)
        self.ui.tblProducts.setColumnCount(2)


        self.ui.tblProducts.setItem(0,0,QTableWidgetItem('Samsung s5'))
        self.ui.tblProducts.setItem(0,1,QTableWidgetItem('2000'))
        self.ui.tblProducts.setItem(1,0,QTableWidgetItem('Asus Zenfone'))
        self.ui.tblProducts.setItem(1,1,QTableWidgetItem('3500'))
        '''
def App():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.setWindowTitle('Tablo uygulaması')
    win.show()
    sys.exit(app.exec_())

App()