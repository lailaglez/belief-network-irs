from PyQt4.QtGui import *
from UI.main import Ui_MainWindow
from modeling import BeliefNetwork
import evaluating
import subprocess
import sys
import os
import processing
import retroalimentation


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.browseBtn.clicked.connect(self.on_browse_clicked)
        self.buildBtn.clicked.connect(self.on_build_clicked)
        self.queryBtn.clicked.connect(self.on_query_clicked)
        self.expandQueryChB.clicked.connect(self.on_expand_query_clicked)
        self.feedBackBtn.clicked.connect(self.on_feedback_clicked)
        self.resultslistWidget.doubleClicked.connect(self.open_file)
        self.numberSpinBox.valueChanged.connect(self.count_change)

        self.groupBoxExpanded.setVisible(False)
        self.inferedLabel.setVisible(False)
        languages = list(processing.languages_available)
        languages.append("infer")
        self.languagesCB.addItems(languages)
        self.languagesCB.setCurrentIndex(languages.index("english"))
        self.dir = None

        self.numberSpinBox.setValue(5)
        self.belief_network = BeliefNetwork()

    def open_file(self):
        doc = self.resultslistWidget.currentItem().text().split(':')[0]
        selected_doc = os.path.join(self.folder_path, doc)
        subprocess.run(["xdg-open", selected_doc])

    def on_expand_query_clicked(self):
        self.groupBoxExpanded.setVisible(self.expandQueryChB.isChecked())

    def on_browse_clicked(self):
        self.folder_path = QFileDialog.getExistingDirectory(self, 'Select a folder')
        if self.folder_path:
            self.pathLineEdit.setText(str(self.folder_path))

    def on_build_clicked(self):
        self.folder_path = str(self.pathLineEdit.text())
        # try:
        self.queryBtn.setEnabled(True)

        language = self.languagesCB.currentText() if self.languagesCB.currentText() != 'infer' else None
        res, infered = self.belief_network.build(self.folder_path, language)
        if language is None and res:
            self.inferedLabel.setText("Infered language: " + infered)
            self.inferedLabel.setVisible(True)
        if language is not None:
            self.inferedLabel.setVisible(False)
        self.names = [str(name) for name in os.listdir(self.folder_path) if
                      name.endswith('.pdf') or name.endswith('.txt')]
        # except:
        #     QMessageBox.critical(self, "Error", "Wrong path", QMessageBox.Ok)

    def on_query_clicked(self):
        query = str(self.queryLineEdit.toPlainText())
        count = self.numberSpinBox.value()

        expand_query = self.expandQueryChB.isChecked()
        results, expanded_query = self.belief_network.query(query, expand_query)
        self.expandedLineEdit.setText(" ".join(expanded_query))
        results.sort(key=lambda t: t[1], reverse=True)
        self.full_list = results
        results = results[:min(len(results), count)]

        self.relevant = evaluating.load_results(self.folder_path, query)
        retrieved = [r[0] for r in results]

        self.print_stats(self.relevant, retrieved)
        self.print_results(results)

    def on_feedback_clicked(self):
        if not self.resultslistWidget.selectedItems():
            QMessageBox.critical(self, "Error", "Select relevant documents.", QMessageBox.Ok)
        else:
            count = self.numberSpinBox.value()
            selected_docs = [i.text().split(':')[0] for i in self.resultslistWidget.selectedItems()]
            new_list = retroalimentation.retroalimentation(self.full_list, selected_docs, self.belief_network)
            self.full_list = new_list
            new_list = new_list[:min(len(new_list), count)]

            self.print_results(new_list)

            self.print_stats(self.relevant, [r[0] for r in new_list])

    def count_change(self):
        count = self.numberSpinBox.value()
        new_list = self.full_list[:count]
        self.print_results(new_list)
        self.print_stats(self.relevant, [r[0] for r in new_list])

    def print_stats(self, relevant, retrieved):
        a = ["precision", "recall", "f_measure", "e_measure"]
        if relevant:
            eval = evaluating.evaluate(relevant_documents=relevant, retrieved_documents=retrieved)
            for ind, v in enumerate(a):
                print(v + ": " + str(eval[v]))
                item = QTableWidgetItem("%.5f" % (eval[v]))
                self.tableWidget.setItem(0, ind, item)

    def print_results(self, results):
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
