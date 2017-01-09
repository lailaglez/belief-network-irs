# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
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
        MainWindow.resize(775, 632)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(9, 9, 731, 98))
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.browseBtn = QtGui.QPushButton(self.groupBox)
        self.browseBtn.setObjectName(_fromUtf8("browseBtn"))
        self.gridLayout_2.addWidget(self.browseBtn, 0, 1, 1, 1)
        self.buildBtn = QtGui.QPushButton(self.groupBox)
        self.buildBtn.setObjectName(_fromUtf8("buildBtn"))
        self.gridLayout_2.addWidget(self.buildBtn, 1, 1, 1, 1)
        self.pathLineEdit = QtGui.QLineEdit(self.groupBox)
        self.pathLineEdit.setObjectName(_fromUtf8("pathLineEdit"))
        self.gridLayout_2.addWidget(self.pathLineEdit, 0, 0, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(9, 219, 731, 228))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.resultslistWidget = QtGui.QListWidget(self.groupBox_3)
        self.resultslistWidget.setObjectName(_fromUtf8("resultslistWidget"))
        self.verticalLayout.addWidget(self.resultslistWidget)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(9, 113, 731, 100))
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.queryBtn = QtGui.QPushButton(self.groupBox_2)
        self.queryBtn.setEnabled(False)
        self.queryBtn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.queryBtn.setObjectName(_fromUtf8("queryBtn"))
        self.gridLayout.addWidget(self.queryBtn, 0, 3, 1, 1)
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.numberSpinBox = QtGui.QSpinBox(self.groupBox_2)
        self.numberSpinBox.setProperty("value", 5)
        self.numberSpinBox.setObjectName(_fromUtf8("numberSpinBox"))
        self.gridLayout.addWidget(self.numberSpinBox, 1, 1, 1, 1)
        self.queryLineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.queryLineEdit.setObjectName(_fromUtf8("queryLineEdit"))
        self.gridLayout.addWidget(self.queryLineEdit, 0, 0, 1, 3)
        spacerItem = QtGui.QSpacerItem(358, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 450, 731, 141))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.statisticslistWidget = QtGui.QListWidget(self.groupBox_4)
        self.statisticslistWidget.setObjectName(_fromUtf8("statisticslistWidget"))
        self.verticalLayout_4.addWidget(self.statisticslistWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 775, 25))
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
        self.buildBtn.setText(_translate("MainWindow", "Build Index", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Results", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Query", None))
        self.queryBtn.setText(_translate("MainWindow", "Search", None))
        self.label.setText(_translate("MainWindow", "Number of results", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Statistics", None))

