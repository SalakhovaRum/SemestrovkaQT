# Form implementation generated from reading ui file 'design_expectation.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class ExpectationDesign(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1030, 720)
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
        self.status = QtWidgets.QLabel(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(-10, 300, 1031, 51))
        self.status.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.status.setObjectName("status")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gallows"))
        self.status.setText(_translate("MainWindow", "We have some time to wait..."))