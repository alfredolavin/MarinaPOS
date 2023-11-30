# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'item_widgetUEYLiY.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_lista_productos_item(object):
    def setupUi(self, lista_productos_item):
        if not lista_productos_item.objectName():
            lista_productos_item.setObjectName(u"lista_productos_item")
        lista_productos_item.resize(497, 50)
        lista_productos_item.setStyleSheet(u"background-color: rgb(252, 240, 240);")
        self.horizontalLayout = QHBoxLayout(lista_productos_item)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.item_indice = QLabel(lista_productos_item)
        self.item_indice.setObjectName(u"item_indice")
        font = QFont()
        font.setFamily(u"Roboto Mono for Powerline")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.item_indice.setFont(font)
        self.item_indice.setStyleSheet(u"border: none;")
        self.item_indice.setTextFormat(Qt.PlainText)

        self.horizontalLayout.addWidget(self.item_indice)

        self.line = QFrame(lista_productos_item)
        self.line.setObjectName(u"line")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QSize(5, 0))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setWeight(50)
        self.line.setFont(font1)
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setFrameShape(QFrame.VLine)

        self.horizontalLayout.addWidget(self.line)

        self.item_cantidad = QLabel(lista_productos_item)
        self.item_cantidad.setObjectName(u"item_cantidad")
        self.item_cantidad.setMinimumSize(QSize(40, 0))
        font2 = QFont()
        font2.setFamily(u"Roboto Mono for Powerline")
        font2.setPointSize(18)
        font2.setBold(False)
        font2.setWeight(50)
        self.item_cantidad.setFont(font2)
        self.item_cantidad.setStyleSheet(u"border: none;")
        self.item_cantidad.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.item_cantidad)

        self.item_descripcion = QLabel(lista_productos_item)
        self.item_descripcion.setObjectName(u"item_descripcion")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.item_descripcion.sizePolicy().hasHeightForWidth())
        self.item_descripcion.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setFamily(u"Ubuntu Light")
        font3.setPointSize(12)
        self.item_descripcion.setFont(font3)
        self.item_descripcion.setStyleSheet(u"border: none;")

        self.horizontalLayout.addWidget(self.item_descripcion)

        self.item_subtotal = QLabel(lista_productos_item)
        self.item_subtotal.setObjectName(u"item_subtotal")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.item_subtotal.sizePolicy().hasHeightForWidth())
        self.item_subtotal.setSizePolicy(sizePolicy2)
        font4 = QFont()
        font4.setFamily(u"Ubuntu Light")
        font4.setPointSize(14)
        self.item_subtotal.setFont(font4)
        self.item_subtotal.setStyleSheet(u"border: none;")

        self.horizontalLayout.addWidget(self.item_subtotal)

        self.item_cantidad.raise_()
        self.item_subtotal.raise_()
        self.item_indice.raise_()
        self.line.raise_()
        self.item_descripcion.raise_()

        self.retranslateUi(lista_productos_item)

        QMetaObject.connectSlotsByName(lista_productos_item)
    # setupUi

    def retranslateUi(self, lista_productos_item):
        lista_productos_item.setWindowTitle(QCoreApplication.translate("lista_productos_item", u"Form", None))
        self.item_indice.setText(QCoreApplication.translate("lista_productos_item", u"A", None))
        self.item_cantidad.setText(QCoreApplication.translate("lista_productos_item", u"2X", None))
        self.item_descripcion.setText(QCoreApplication.translate("lista_productos_item", u"ACIDO MEFENAMICO 500MG X 10 COM\n"
" $ 1.500.-", None))
        self.item_subtotal.setText(QCoreApplication.translate("lista_productos_item", u"$   3.000", None))
    # retranslateUi

