# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_principal_ventasPNEhMF.ui'
##
## Created by: Qt User Interface Compiler version 5.15.10
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
        MainWindow.resize(453, 433)
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
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setStyleSheet(u"background-color: rgb(252, 240, 240);\n"
"border-radius: 8px;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 441, 375))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.item_descripcion = QLabel(self.scrollAreaWidgetContents)
        self.item_descripcion.setObjectName(u"item_descripcion")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.item_descripcion.sizePolicy().hasHeightForWidth())
        self.item_descripcion.setSizePolicy(sizePolicy2)
#if QT_CONFIG(tooltip)
        self.item_descripcion.setToolTip(u"")
#endif // QT_CONFIG(tooltip)

        self.verticalLayout_2.addWidget(self.item_descripcion)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy2.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy2)
#if QT_CONFIG(tooltip)
        self.widget.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.widget.setStyleSheet(u"background-color: rgb(206, 212, 255);\n"
"border-radius: 15px;")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        font = QFont()
        font.setFamily(u"Roboto Mono for Powerline")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
#if QT_CONFIG(tooltip)
        self.label.setToolTip(u"")
#endif // QT_CONFIG(tooltip)

        self.horizontalLayout_2.addWidget(self.label)

        self.main_input = QLineEdit(self.widget)
        self.main_input.setObjectName(u"main_input")
        sizePolicy1.setHeightForWidth(self.main_input.sizePolicy().hasHeightForWidth())
        self.main_input.setSizePolicy(sizePolicy1)
        self.main_input.setMaximumSize(QSize(173, 16777215))
        font1 = QFont()
        font1.setFamily(u"Roboto Mono for Powerline")
        font1.setPointSize(15)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.main_input.setFont(font1)
#if QT_CONFIG(tooltip)
        self.main_input.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.main_input.setStyleSheet(u"border-radius: 15px;\n"
"border: 1px dotted black;")
        self.main_input.setMaxLength(14)
        self.main_input.setFrame(False)
        self.main_input.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.main_input)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy4)
        self.label_4.setFont(font)
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
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
        self.item_descripcion.setText(QCoreApplication.translate("MainWindow", u"<p style=\"font:\\'Roboto Mono Light for Powerline\\'; font-size:11pt; font-weight:200;\"><span style=\" font-weight:792;\"><span style=\"font-weight:792; color:#ff0000;border-left: 3px;\">A</span></span>&nbsp;&nbsp;&nbsp;&nbsp;ACIDO MEFENAMICO 500MG X 10 COM&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style=\" font-weight:600;\">$ 3.000.-</span><br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style=\" font-weight:200;color:#ff0000;\">2X </span>$ 1.500.-<br /></p>", None))
        self.label.setText("")
        self.main_input.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Total: $  3.400.-", None))
    # retranslateUi

