# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_principal_ventasRkaHFZ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(543, 433)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ListaItemsVenta = QListWidget(self.centralwidget)
        self.ListaItemsVenta.setObjectName(u"ListaItemsVenta")
        self.ListaItemsVenta.setFocusPolicy(Qt.NoFocus)
        self.ListaItemsVenta.setStyleSheet(u"background-color: rgb(252, 240, 240);\n"
"border-radius: 15px;")

        self.verticalLayout.addWidget(self.ListaItemsVenta)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.widget.setStyleSheet(u"background-color: rgb(206, 212, 255);\n"
"border-radius: 15px;")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setFamily(u"Roboto Mono for Powerline")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)

        self.main_input = QLineEdit(self.widget)
        self.main_input.setObjectName(u"main_input")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.main_input.sizePolicy().hasHeightForWidth())
        self.main_input.setSizePolicy(sizePolicy3)
        font1 = QFont()
        font1.setFamily(u"Roboto Mono Thin for Powerline")
        font1.setPointSize(29)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.main_input.setFont(font1)
        self.main_input.setStyleSheet(u"border-radius: 15px;\n"
"border: 1px dotted black;")
        self.main_input.setMaxLength(16)
        self.main_input.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.main_input)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy4)
        font2 = QFont()
        font2.setFamily(u"Roboto Mono for Powerline")
        font2.setPointSize(19)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_4.setFont(font2)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet(u"")
        self.label_4.setTextFormat(Qt.PlainText)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_4)


        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.main_input.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Total: $  3.400.-", None))
    # retranslateUi

