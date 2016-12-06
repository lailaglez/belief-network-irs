import modeling
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
from UI.main import Ui_MainWindow



# Se llama cuando se cambia el path en la UI
def build(path):
    modeling.build(path)


# Se llama cuando se realiza una query desde la UI, count es el número de resultados deseados
def query(query, count):
    return modeling.query(query, count)



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        print("button")
        self.label.setText(self.lineEdit.text())

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()


