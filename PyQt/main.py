# File: main.py
import sys
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QListWidgetItem, QWidget, QListWidget
from PySide2.QtCore import QFile, QIODevice


def crea_producto_widget(padre: QListWidget, cantidad: int, descripcion: str, precio: int):
  global item_widget
  mi_copia = item_widget
  mi_item = QListWidgetItem(padre)
  mi_copia.item_cantidad.setText(str(cantidad))
  mi_copia.item_descripcion.setText(descripcion)
  #mi_copia.item_precio.setText(str(precio))
  mi_copia.item_subtotal.setText(str(cantidad*precio))
  mi_item.setSizeHint(mi_copia.sizeHint())
  padre.addItem(mi_item)
  padre.setItemWidget(mi_item, mi_copia)
  return mi_copia


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
  
  
  item_widget_file_name = "item_widget.ui"
  item_widget_file = QFile(item_widget_file_name)
  if not item_widget_file.open(QIODevice.ReadOnly):
    print("Cannot open {}: {}".format(item_widget_file_name, item_widget_file.errorString()))
    sys.exit(-1)  
  loader = QUiLoader()
  item_widget = loader.load(item_widget_file) 
  item_widget_file.close()
  crea_producto_widget(window.ListaItemsVenta, 3, "AMOXICILINA 500MG X 21CAP\n$  5.000.-", 1200)
  crea_producto_widget(window.ListaItemsVenta, 2, "DICLOFENACO 100MG X 10CAP\n$  2.000.-", 1000)
      
  
  
 
 
 
  sys.exit(app.exec_())