import sys
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QListWidgetItem, QWidget, QListWidget, QLabel
from PySide2.QtCore import QFile, QIODevice

app=QApplication([])

class TextBrowser(QLabel):
    def __init__ (self, parent = None):
        super(TextBrowser, self).__init__(parent)

listWidget = QListWidget()
for i in range(5):
    item = QListWidgetItem(listWidget)
    itemWidget = TextBrowser()
    itemWidget.setText(u"<p style=\"font:'Roboto Mono Light for Powerline'; font-size:11pt; font-weight:200;\"><span style=\" font-weight:792;\">A&nbsp;&nbsp;&nbsp;&nbsp;</span>ACIDO MEFENAMICO 500MG X 10 COM<span style=\" font-weight:600;\">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$ 3.000.-</span><br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style=\" font-weight:600;\">2X </span>$ 1.500.-<br /></p>")
    item.setSizeHint(itemWidget.sizeHint())
    listWidget.setItemWidget(item, itemWidget)

listWidget.show()
app.exec_()