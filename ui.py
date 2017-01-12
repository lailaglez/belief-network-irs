from PyQt4.QtGui import *
from UI.main import Ui_MainWindow
from modeling import BeliefNetwork
import evaluating
import sys
import os
import processing


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.browseBtn.clicked.connect(self.on_browse_clicked)
        self.buildBtn.clicked.connect(self.on_build_clicked)
        self.queryBtn.clicked.connect(self.on_query_clicked)
        self.expandQueryChB.clicked.connect(self.on_expand_query_clicked)

        self.groupBoxExpanded.setVisible(False)
        languages = list(processing.languages_available)
        languages.append("infer")
        self.languagesCB.addItems(languages)
        self.languagesCB.setCurrentIndex(languages.index("english"))
        self.dir = None

        self.belief_network = BeliefNetwork()

    def on_expand_query_clicked(self):
        self.groupBoxExpanded.setVisible(self.expandQueryChB.isChecked())

    def on_browse_clicked(self):
        self.folder_path = QFileDialog.getExistingDirectory(self, 'Select a folder')
        if self.folder_path:
            self.pathLineEdit.setText(str(self.folder_path))

    def on_build_clicked(self):
        self.folder_path = str(self.pathLineEdit.text())
        try:
            self.queryBtn.setEnabled(True)

            language_combo_text = self.languagesCB.currentText()
            language = language_combo_text if language_combo_text != 'infer' else None

            self.belief_network.build(self.folder_path, language)
            self.names = [str(name) for name in os.listdir(self.folder_path) if name.endswith('.pdf') or name.endswith('.txt')]
        except:
            QMessageBox.critical(self, "Error", "Wrong path", QMessageBox.Ok)

    def on_query_clicked(self):
        query = str(self.queryLineEdit.toPlainText())
        count = self.numberSpinBox.value()

        expand_query = self.expandQueryChB.isChecked()

        results, expanded_query = self.belief_network.query(query, expand_query)
        results.sort(key=lambda t: t[1], reverse=True)
        results = results[:min(len(results), count)]

        self.expandedLineEdit.setText(" ".join(expanded_query))

        relevant = evaluating.load_results(self.folder_path, query)
        retrieved = [r[0] for r in results]

        if relevant:
            eval = evaluating.evaluate(relevant_documents=relevant, retrieved_documents=retrieved)
            self.statisticslistWidget.clear()
            self.statisticslistWidget.addItems([str(k) + ': ' + str(v) for k, v in eval.items()])

        self.resultslistWidget.clear()

        if results:
            self.resultslistWidget.addItems([str(t[0]) + ': ' + str(t[1]) for t in results])
        else:
            self.resultslistWidget.addItem('No results.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec_()