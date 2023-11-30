# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_principal_ventascptAHQ.ui'
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
		self.centralwidget = QWidget(MainWindow)
		self.centralwidget.setObjectName(u"centralwidget")
		self.verticalLayout = QVBoxLayout(self.centralwidget)
		self.verticalLayout.setObjectName(u"verticalLayout")
		self.horizontalLayout = QHBoxLayout()
		self.horizontalLayout.setObjectName(u"horizontalLayout")
		self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.horizontalLayout.addItem(self.horizontalSpacer)

		self.label = QLabel(self.centralwidget)
		self.label.setObjectName(u"label")
		sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
		self.label.setSizePolicy(sizePolicy)
		font = QFont()
		font.setFamily(u"Roboto Mono for Powerline")
		font.setPointSize(26)
		font.setBold(True)
		font.setWeight(75)
		self.label.setFont(font)

		self.horizontalLayout.addWidget(self.label)

		self.lineEdit = QLineEdit(self.centralwidget)
		self.lineEdit.setObjectName(u"lineEdit")
		font1 = QFont()
		font1.setFamily(u"Roboto Mono Thin for Powerline")
		font1.setPointSize(29)
		font1.setBold(False)
		font1.setItalic(False)
		font1.setWeight(50)
		self.lineEdit.setFont(font1)
		self.lineEdit.setStyleSheet(u"border-radius: 20px;\n"
"border: 1px solid black;")
		self.lineEdit.setMaxLength(16)
		self.lineEdit.setFrame(True)
		self.lineEdit.setAlignment(Qt.AlignCenter)

		self.horizontalLayout.addWidget(self.lineEdit)

		self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		self.horizontalLayout.addItem(self.horizontalSpacer_2)


		self.verticalLayout.addLayout(self.horizontalLayout)

		self.label_3 = QLabel(self.centralwidget)
		self.label_3.setObjectName(u"label_3")
		sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
		sizePolicy1.setHorizontalStretch(0)
		sizePolicy1.setVerticalStretch(0)
		sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
		self.label_3.setSizePolicy(sizePolicy1)
		self.label_3.setMinimumSize(QSize(0, 40))
		self.label_3.setStyleSheet(u"padding: 0 0 10 10")
		self.label_3.setTextFormat(Qt.PlainText)
		self.label_3.setScaledContents(False)
#        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
		self.label_3.setWordWrap(True)

		self.verticalLayout.addWidget(self.label_3)

		self.ListaItemsVenta = QScrollArea(self.centralwidget)
		self.ListaItemsVenta.setObjectName(u"ListaItemsVenta")
		font2 = QFont()
		font2.setFamily(u"Roboto Mono for Powerline")
		font2.setPointSize(16)
		self.ListaItemsVenta.setFont(font2)
		self.ListaItemsVenta.setFocusPolicy(Qt.NoFocus)
		self.ListaItemsVenta.setWidgetResizable(True)
		self.scrollAreaWidgetContents = QWidget()
		self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
		self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 525, 276))
		self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
		self.verticalLayout_2.setObjectName(u"verticalLayout_2")
		self.itemVenta = QWidget(self.scrollAreaWidgetContents)
		self.itemVenta.setObjectName(u"itemVenta")
		sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
		sizePolicy2.setHorizontalStretch(0)
		sizePolicy2.setVerticalStretch(0)
		sizePolicy2.setHeightForWidth(self.itemVenta.sizePolicy().hasHeightForWidth())
		self.itemVenta.setSizePolicy(sizePolicy2)
		font3 = QFont()
		font3.setFamily(u"Ubuntu Light")
		font3.setPointSize(8)
		font3.setBold(False)
		font3.setWeight(50)
		self.itemVenta.setFont(font3)
		self.itemVenta.setStyleSheet(u"border-bottom-color: rgb(160, 160, 160);\n"
"border-style: dotted;\n"
"border-bottom-width: 1px;\n"
"padding-left: 0px;")
		self.horizontalLayout_3 = QHBoxLayout(self.itemVenta)
		self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
		self.label_2 = QLabel(self.itemVenta)
		self.label_2.setObjectName(u"label_2")
		font4 = QFont()
		font4.setFamily(u"Roboto Mono for Powerline")
		font4.setPointSize(18)
		font4.setBold(True)
		font4.setWeight(75)
		self.label_2.setFont(font4)
		self.label_2.setStyleSheet(u"border: none;")
		self.label_2.setTextFormat(Qt.PlainText)

		self.horizontalLayout_3.addWidget(self.label_2)

		self.line = QFrame(self.itemVenta)
		self.line.setObjectName(u"line")
		sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
		sizePolicy3.setHorizontalStretch(0)
		sizePolicy3.setVerticalStretch(0)
		sizePolicy3.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
		self.line.setSizePolicy(sizePolicy3)
		self.line.setMinimumSize(QSize(5, 0))
		font5 = QFont()
		font5.setPointSize(11)
		font5.setBold(False)
		font5.setWeight(50)
		self.line.setFont(font5)
		self.line.setFrameShadow(QFrame.Plain)
		self.line.setFrameShape(QFrame.VLine)

		self.horizontalLayout_3.addWidget(self.line)

		self.label_11 = QLabel(self.itemVenta)
		self.label_11.setObjectName(u"label_11")
		self.label_11.setMinimumSize(QSize(40, 0))
		font6 = QFont()
		font6.setFamily(u"Roboto Mono for Powerline")
		font6.setPointSize(18)
		font6.setBold(False)
		font6.setWeight(50)
		self.label_11.setFont(font6)
		self.label_11.setStyleSheet(u"border: none;")
#        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

		self.horizontalLayout_3.addWidget(self.label_11)

		self.label_6 = QLabel(self.itemVenta)
		self.label_6.setObjectName(u"label_6")
		sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
		sizePolicy4.setHorizontalStretch(0)
		sizePolicy4.setVerticalStretch(0)
		sizePolicy4.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
		self.label_6.setSizePolicy(sizePolicy4)
		font7 = QFont()
		font7.setFamily(u"Ubuntu Light")
		font7.setPointSize(12)
		self.label_6.setFont(font7)
		self.label_6.setStyleSheet(u"border: none;")

		self.horizontalLayout_3.addWidget(self.label_6)

		self.label_8 = QLabel(self.itemVenta)
		self.label_8.setObjectName(u"label_8")
		sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
		sizePolicy5.setHorizontalStretch(0)
		sizePolicy5.setVerticalStretch(0)
		sizePolicy5.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
		self.label_8.setSizePolicy(sizePolicy5)
		font8 = QFont()
		font8.setFamily(u"Ubuntu Light")
		font8.setPointSize(14)
		self.label_8.setFont(font8)
		self.label_8.setStyleSheet(u"border: none;")

		self.horizontalLayout_3.addWidget(self.label_8)


		self.verticalLayout_2.addWidget(self.itemVenta)

		self.ListaItemsVenta.setWidget(self.scrollAreaWidgetContents)

		self.verticalLayout.addWidget(self.ListaItemsVenta)

		self.horizontalLayout_2 = QHBoxLayout()
		self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
		self.label_5 = QLabel(self.centralwidget)
		self.label_5.setObjectName(u"label_5")
		font9 = QFont()
		font9.setFamily(u"Ubuntu")
		font9.setPointSize(15)
		font9.setBold(False)
		font9.setWeight(50)
		self.label_5.setFont(font9)
		self.label_5.setMidLineWidth(0)
		self.label_5.setTextFormat(Qt.PlainText)
#		self.label_5.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
		self.label_5.setMargin(0)
		self.label_5.setIndent(0)

		self.horizontalLayout_2.addWidget(self.label_5)

		self.label_4 = QLabel(self.centralwidget)
		self.label_4.setObjectName(u"label_4")
		sizePolicy6 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
		sizePolicy6.setHorizontalStretch(0)
		sizePolicy6.setVerticalStretch(0)
		sizePolicy6.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
		self.label_4.setSizePolicy(sizePolicy6)
		font10 = QFont()
		font10.setFamily(u"Roboto Mono for Powerline")
		font10.setPointSize(16)
		font10.setBold(True)
		font10.setWeight(75)
		self.label_4.setFont(font10)
		self.label_4.setTextFormat(Qt.PlainText)
#		self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

		self.horizontalLayout_2.addWidget(self.label_4)


		self.verticalLayout.addLayout(self.horizontalLayout_2)

		MainWindow.setCentralWidget(self.centralwidget)

		self.retranslateUi(MainWindow)

		QMetaObject.connectSlotsByName(MainWindow)
	# setupUi

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
		self.label.setText("")
		self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"7800007176394", None))
		self.label_3.setText(QCoreApplication.translate("MainWindow", u"Lista vac\u00eda. Escan\u00e9e un producto, Ingrese multiplicador o c\u00f3digo producto,", None))
		self.label_2.setText(QCoreApplication.translate("MainWindow", u"A", None))
		self.label_11.setText(QCoreApplication.translate("MainWindow", u"2X", None))
		self.label_6.setText(QCoreApplication.translate("MainWindow", u"ACIDO MEFENAMICO 500MG X 10 COM\n"
" $ 1.500.-", None))
		self.label_8.setText(QCoreApplication.translate("MainWindow", u"$   3.000", None))
		self.label_5.setText(QCoreApplication.translate("MainWindow", u"Venta Actual:", None))
		self.label_4.setText(QCoreApplication.translate("MainWindow", u"$  3.400.-", None))
	# retranslateUi
