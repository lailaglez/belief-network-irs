# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Schools\Universidad\5to ano\1er Semestre\Sistema de informacion\SI-Amalia-Laila-Jose\UI\main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(773, 674)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pathLineEdit = QtGui.QLineEdit(self.groupBox)
        self.pathLineEdit.setObjectName(_fromUtf8("pathLineEdit"))
        self.gridLayout_2.addWidget(self.pathLineEdit, 0, 0, 1, 4)
        self.browseBtn = QtGui.QPushButton(self.groupBox)
        self.browseBtn.setObjectName(_fromUtf8("browseBtn"))
        self.gridLayout_2.addWidget(self.browseBtn, 0, 4, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.languagesCB = QtGui.QComboBox(self.groupBox)
        self.languagesCB.setObjectName(_fromUtf8("languagesCB"))
        self.gridLayout_2.addWidget(self.languagesCB, 1, 1, 1, 1)
        self.inferedLabel = QtGui.QLabel(self.groupBox)
        self.inferedLabel.setObjectName(_fromUtf8("inferedLabel"))
        self.gridLayout_2.addWidget(self.inferedLabel, 1, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(260, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 3, 1, 1)
        self.buildBtn = QtGui.QPushButton(self.groupBox)
        self.buildBtn.setObjectName(_fromUtf8("buildBtn"))
        self.gridLayout_2.addWidget(self.buildBtn, 1, 4, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.queryBtn = QtGui.QPushButton(self.groupBox_2)
        self.queryBtn.setEnabled(False)
        self.queryBtn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.queryBtn.setObjectName(_fromUtf8("queryBtn"))
        self.gridLayout.addWidget(self.queryBtn, 0, 4, 1, 1)
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.numberSpinBox = QtGui.QSpinBox(self.groupBox_2)
        self.numberSpinBox.setMaximum(9999999)
        self.numberSpinBox.setProperty("value", 0)
        self.numberSpinBox.setObjectName(_fromUtf8("numberSpinBox"))
        self.gridLayout.addWidget(self.numberSpinBox, 1, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(358, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.expandQueryChB = QtGui.QCheckBox(self.groupBox_2)
        self.expandQueryChB.setObjectName(_fromUtf8("expandQueryChB"))
        self.gridLayout.addWidget(self.expandQueryChB, 1, 3, 1, 1)
        self.queryLineEdit = QtGui.QTextEdit(self.groupBox_2)
        self.queryLineEdit.setMaximumSize(QtCore.QSize(16777215, 42))
        self.queryLineEdit.setDocumentTitle(_fromUtf8(""))
        self.queryLineEdit.setReadOnly(False)
        self.queryLineEdit.setObjectName(_fromUtf8("queryLineEdit"))
        self.gridLayout.addWidget(self.queryLineEdit, 0, 0, 1, 4)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBoxExpanded = QtGui.QGroupBox(self.centralwidget)
        self.groupBoxExpanded.setObjectName(_fromUtf8("groupBoxExpanded"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBoxExpanded)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.expandedLineEdit = QtGui.QTextEdit(self.groupBoxExpanded)
        self.expandedLineEdit.setMaximumSize(QtCore.QSize(16777215, 42))
        self.expandedLineEdit.setReadOnly(True)
        self.expandedLineEdit.setObjectName(_fromUtf8("expandedLineEdit"))
        self.horizontalLayout.addWidget(self.expandedLineEdit)
        self.verticalLayout_3.addWidget(self.groupBoxExpanded)
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.resultslistWidget = QtGui.QListWidget(self.groupBox_3)
        self.resultslistWidget.setObjectName(_fromUtf8("resultslistWidget"))
        self.gridLayout_3.addWidget(self.resultslistWidget, 0, 0, 1, 2)
        spacerItem2 = QtGui.QSpacerItem(651, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 1, 0, 1, 1)
        self.feedBackBtn = QtGui.QPushButton(self.groupBox_3)
        self.feedBackBtn.setObjectName(_fromUtf8("feedBackBtn"))
        self.gridLayout_3.addWidget(self.feedBackBtn, 1, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tableWidget = QtGui.QTableWidget(self.groupBox_4)
        self.tableWidget.setMaximumSize(QtCore.QSize(411, 55))
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout_3.addWidget(self.groupBox_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 773, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox.setTitle(_translate("MainWindow", "Indexed folder path", None))
        self.browseBtn.setText(_translate("MainWindow", "Browse...", None))
        self.label_2.setText(_translate("MainWindow", "Languages available", None))
        self.inferedLabel.setText(_translate("MainWindow", "Language infered:", None))
        self.buildBtn.setText(_translate("MainWindow", "Build Index", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Query", None))
        self.queryBtn.setText(_translate("MainWindow", "Search", None))
        self.label.setText(_translate("MainWindow", "Number of results", None))
        self.expandQueryChB.setText(_translate("MainWindow", "Expand query", None))
        self.groupBoxExpanded.setTitle(_translate("MainWindow", "Expanded Query", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Results", None))
        self.feedBackBtn.setText(_translate("MainWindow", "Feedback", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Statistics", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Precision", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Recall", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "F_measure", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "E_measure", None))

