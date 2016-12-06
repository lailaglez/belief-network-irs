# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/jose/Storage/Schools/Universidad/5to ano/1er Semestre/Sistema de informacion/SI-Amalia-Laila-Jose/UI/main.ui'
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
        MainWindow.resize(694, 623)
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
        self.gridLayout_2.addWidget(self.pathLineEdit, 0, 0, 1, 1)
        self.browseBtn = QtGui.QPushButton(self.groupBox)
        self.browseBtn.setObjectName(_fromUtf8("browseBtn"))
        self.gridLayout_2.addWidget(self.browseBtn, 0, 1, 1, 1)
        self.buildBtn = QtGui.QPushButton(self.groupBox)
        self.buildBtn.setObjectName(_fromUtf8("buildBtn"))
        self.gridLayout_2.addWidget(self.buildBtn, 1, 1, 1, 1)
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
        self.gridLayout.addWidget(self.queryBtn, 0, 3, 1, 1)
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.numberSpinBox = QtGui.QSpinBox(self.groupBox_2)
        self.numberSpinBox.setProperty("value", 5)
        self.numberSpinBox.setObjectName(_fromUtf8("numberSpinBox"))
        self.gridLayout.addWidget(self.numberSpinBox, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(358, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.queryLineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.queryLineEdit.setObjectName(_fromUtf8("queryLineEdit"))
        self.gridLayout.addWidget(self.queryLineEdit, 0, 0, 1, 3)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.resultslistWidget = QtGui.QListWidget(self.groupBox_3)
        self.resultslistWidget.setObjectName(_fromUtf8("resultslistWidget"))
        self.verticalLayout.addWidget(self.resultslistWidget)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayout_3.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 694, 25))
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
        self.groupBox_2.setTitle(_translate("MainWindow", "Query", None))
        self.queryBtn.setText(_translate("MainWindow", "Search", None))
        self.label.setText(_translate("MainWindow", "Number of results", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Results", None))
        self.label_2.setText(_translate("MainWindow", "Lugar destinado para mostrar las evaluaciones de la busqueda", None))

