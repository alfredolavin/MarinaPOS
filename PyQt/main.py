# File: main.py
import sys
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QListWidgetItem, QWidget, QListWidget
from PySide2.QtCore import QFile, QIODevice

if __name__ == "__main__":
  app = QApplication(sys.argv)

  ui_file_name = "ventana_principal_ventas.ui"
  ui_file = QFile(ui_file_name)
  if not ui_file.open(QIODevice.ReadOnly):
    print("Cannot open {}: {}".format(ui_file_name, ui_file.errorString()))
    sys.exit(-1)  
  loader = QUiLoader()
  window = loader.load(ui_file)
  ui_file.close()
 
  if not window:
    print(loader.errorString())
    sys.exit(-1)
  window.show()
  window.main_input.returnPressed.connect(lambda : print(window.main_input.text()))
  app.exec_()