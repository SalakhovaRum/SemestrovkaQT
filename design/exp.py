# Form implementation generated from reading ui file 'expectation.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow3(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1195, 827)
        MainWindow.setStyleSheet("QWidget {\n"
                                 "    color: white;\n"
                                 "    background-color: #121212;\n"
                                 "    font-family: Rubik;\n"
                                 "    font-size: 16pt;\n"
                                 "    font-weight: 600;\n"
                                 "}\n"
                                 "QPushButton {\n"
                                 "    background-color: green;\n"
                                 "    border: none;\n"
                                 "}\n"
                                 "QPushButton:hover {\n"
                                 "    background-color: #7CFC00;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "    background-color: #228B22;\n"
                                 "}\n"
                                 "\n"
                                 "pushButton {\n"
                                 "    background-color: white;\n"
                                 "    border: none;\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 1191, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.status = QtWidgets.QLabel(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(10, 250, 1181, 51))
        self.status.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.status.setObjectName("status")
        self.status_2 = QtWidgets.QLabel(self.centralwidget)
        self.status_2.setGeometry(QtCore.QRect(10, 330, 1181, 51))
        self.status_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.status_2.setObjectName("status_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gallows"))
        self.label.setText(_translate("MainWindow", "ВИСЕЛИЦА"))
        self.status.setText(_translate("MainWindow", "ИГРА СКОРО НАЧНЕТСЯ"))
        self.status_2.setText(_translate("MainWindow", "ПЕРВЫЙ ИГРОК ВЫБИРАЕТ РЕЖИМ"))
