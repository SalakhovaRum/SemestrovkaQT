# Form implementation generated from reading ui file 'design_end.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class EndDesign(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1029, 721)
        MainWindow.setStyleSheet("QWidget {\n"
                                 "    color: #4169E1;\n"
                                 "    background-color: #ADD8E6;\n"
                                 "    font-family: Rubik;\n"
                                 "    font-size: 16pt;\n"
                                 "    font-weight: 600;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton {\n"
                                 "    background-color: #1E90FF;\n"
                                 "    border: none;\n"
                                 "}\n"
                                 "QPushButton:hover {\n"
                                 "    background-color: #00BFFF;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "    background-color:#0000FF;\n"
                                 "}\n"
                                 "\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 310, 571, 101))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 20, 791, 61))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 450, 571, 101))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 311, 31))
        self.label_3.setObjectName("label_3")
        self.word = QtWidgets.QLabel(self.centralwidget)
        self.word.setGeometry(QtCore.QRect(450, 140, 571, 31))
        self.word.setObjectName("word")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Play"))
        self.label.setText(_translate("MainWindow", "ВЫ ПРОИГРАЛИ/ПОБУДИЛИ"))
        self.pushButton_2.setText(_translate("MainWindow", "Exit"))
        self.label_3.setText(_translate("MainWindow", "Hidden word:"))
        self.word.setText(_translate("MainWindow", "WORD"))
