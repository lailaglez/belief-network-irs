import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
from UI.main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.browseBtn.clicked.connect(self.on_browse_clicked)
        self.buildBtn.clicked.connect(self.on_build_clicked)
        self.queryBtn.clicked.connect(self.on_query_clicked)

        self.dir = None

    def on_browse_clicked(self):
        self.folder_path = QFileDialog.getExistingDirectory(self, 'Select a folder')
        if self.folder_path:
            self.pathLineEdit.setText(str(self.folder_path))

    def on_build_clicked(self):
        self.folder_path = str(self.pathLineEdit.text())
        print(self.folder_path)
        try:
            # modeling.build(self.folder_path)
            self.names = [str(name) for name in os.listdir(self.folder_path) if name.endswith('.pdf') or name.endswith('.txt')]
            self.queryBtn.setEnabled(True)
        except:
            QMessageBox.critical(self, "Error", "Wrong path", QMessageBox.Ok)

    def on_query_clicked(self):
        query = str(self.queryLineEdit.text())
        count = self.numberSpinBox.value()
        # modeling.query(query, count)

        results = [name for name in self.names if name.find(query) >= 0]
        self.resultslistWidget.clear()
        self.resultslistWidget.addItems(results[0:min(len(results), count)])

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()


