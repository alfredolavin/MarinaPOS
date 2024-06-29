import sys
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QListWidgetItem, QWidget, QListWidget, QLabel
from PySide2.QtCore import QFile, QIODevice

test = \
""" <table cellpadding="0" cellspacing="0" data-sheets-root="1" dir="ltr" style="table-layout: fixed; font-size: 10pt; font-family: Roboto; width: 0px;" xmlns="http://www.w3.org/1999/xhtml">
	<colgroup>
		<col width="158" />
		<col width="51" />
		<col width="306" />
		<col width="197" />
	</colgroup>
	<tbody>
		<tr style="height: 46px;">
			<td data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0;\&quot;  PAGO:\&quot;* \&quot;$\&quot;#,##0\&quot;.\&quot;-;;@&quot;,&quot;3&quot;:1}" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:7800028210350}" style="border-right: 1px solid rgb(255, 0, 0); border-bottom: 1px solid rgb(217, 217, 217); border-left: 1px solid rgb(255, 0, 0); overflow: hidden; padding: 0px 3px; vertical-align: middle; background-color: rgb(252, 240, 240); font-family: &quot;Roboto Mono&quot;; font-size: 11pt; overflow-wrap: break-word; text-align: center;">7800028210350</td>
			<td data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;[&gt;1]#\&quot;X\&quot;;;;&quot;,&quot;3&quot;:1}" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:1}" style="border-top: 1px solid rgb(217, 217, 217); border-bottom: 1px solid rgb(217, 217, 217); overflow: hidden; padding: 0px 3px; vertical-align: middle; background-color: rgb(252, 240, 240);">&nbsp;</td>
			<td data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;;;;@&quot;}" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;NASTIZOL COMPOSITUM 100ML JBE.\n $ 12.000.-&quot;}" style="border-top: 1px solid rgb(217, 217, 217); border-right: 1px solid rgb(255, 0, 0); border-bottom: 1px solid rgb(217, 217, 217); overflow: hidden; padding: 0px 3px; vertical-align: middle; background-color: rgb(252, 240, 240); font-family: &quot;Roboto Mono&quot;; font-size: 11pt;">NASTIZOL COMPOSITUM 100ML JBE.<br />
			$ 12.000.-</td>
			<td data-sheets-formula="=IFS(R[0]C[4];R[0]C[15];R[0]C[10];R[0]C[10];VERDADERO;&quot;&quot;)" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;$* #,##0;$ #,##0.-;\&quot;\&quot;;@&quot;,&quot;3&quot;:1}" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:12000}" style="border-top: 1px solid rgb(217, 217, 217); border-right: 1px solid rgb(255, 0, 0); border-bottom: 1px solid rgb(217, 217, 217); overflow: hidden; padding: 0px 3px; vertical-align: middle; background-color: rgb(252, 240, 240); font-family: &quot;Roboto Mono&quot;; font-size: 13pt; text-align: right;">$ 12.000</td>
		</tr>
		<tr style="height: 46px;">
			<td data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;0;\&quot;  PAGO:\&quot;* \&quot;$\&quot;#,##0\&quot;.\&quot;-;;@&quot;,&quot;3&quot;:1}" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:7800063001524}" style="border-right: 1px solid rgb(255, 0, 0); border-bottom: 1px solid rgb(217, 217, 217); border-left: 1px solid rgb(255, 0, 0); overflow: hidden; padding: 0px 3px; vertical-align: middle; background-color: rgb(255, 228, 228); font-family: &quot;Roboto Mono&quot;; font-size: 11pt; overflow-wrap: break-word; text-align: center;">7800063001524</td>
			<td data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;[&gt;1]#\&quot;X\&quot;;;;&quot;,&quot;3&quot;:1}" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:1}" style="border-bottom: 1px solid rgb(217, 217, 217); overflow: hidden; padding: 0px 3px; vertical-align: middle; background-color: rgb(255, 228, 228);">&nbsp;</td>
			<td data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;;;;@&quot;}" data-sheets-value="{&quot;1&quot;:2,&quot;2&quot;:&quot;BROMFIN 8MG/5ML X 100 ML\n $ 8.000.-&quot;}" style="border-right: 1px solid rgb(255, 0, 0); border-bottom: 1px solid rgb(217, 217, 217); overflow: hidden; padding: 0px 3px; vertical-align: middle; background-color: rgb(255, 228, 228); font-family: &quot;Roboto Mono&quot;; font-size: 11pt;">BROMFIN 8MG/5ML X 100 ML<br />
			$ 8.000.-</td>
			<td data-sheets-formula="=IFS(R[0]C[4];R[0]C[15];R[0]C[10];R[0]C[10];VERDADERO;&quot;&quot;)" data-sheets-numberformat="{&quot;1&quot;:2,&quot;2&quot;:&quot;$* #,##0;$ #,##0.-;\&quot;\&quot;;@&quot;,&quot;3&quot;:1}" data-sheets-value="{&quot;1&quot;:3,&quot;3&quot;:8000}" style="border-right: 1px solid rgb(255, 0, 0); border-bottom: 1px solid rgb(217, 217, 217); overflow: hidden; padding: 0px 3px; vertical-align: middle; background-color: rgb(255, 228, 228); font-family: &quot;Roboto Mono&quot;; font-size: 13pt; text-align: right;">$ 8.000</td>
		</tr>
	</tbody>
</table>"""

formatea_como_dinero = lambda x, y = 6: f'${x:>8,}'.replace(',','.').replace(' ', '&nbsp;')

genera_texto_item = lambda indice, descripcion, cantidad, precio: f'<p style=\"font:\'Roboto Mono Light for Powerline\';font-size:11pt;font-weight:200;\"><span style=\" font-weight:792;\"><span style=\"font-weight:792;font-size:14pt; color:#FF0000;\">{chr(ord("A")+indice)}&nbsp;&nbsp;</span><span style=\" font-weight:600;color:#000000;\">{f"{cantidad:>2} X" if cantidad > 1 else ""}</span></span>&nbsp;{descripcion}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{f"&nbsp;" if cantidad > 1 else "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"}<span style=\" font-weight:800;\">{formatea_como_dinero(precio*cantidad)}.-</span><br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{formatea_como_dinero(precio)}</p>'

if __name__ == "__main__":
  app=QApplication([])
  listWidget = QListWidget()
  listWidget.resize(390, 433)
  listWidget.setStyleSheet(u"")
  ejemplo = (
    ("BETAMETASONA 0.5% X 15 G", 1, 1_500),
    ("SILDENAFILO 50MG X 1 COMP", 5, 1_000),
    ("MODAVITAE 100MG X 30COM", 3, 24_000)
  )
  
  
  for i, [descripcion, cantidad, precio] in enumerate(ejemplo):
    item = QListWidgetItem(listWidget)
    itemWidget = QLabel()
    itemWidget.setStyleSheet(f'padding: 6px; background-color: {"rgb(252, 240, 240)" if i%2 == 0 else "rgb(255, 228, 228)"}; border-bottom: 1px solid rgb(217, 217, 217)')

    itemWidget.setText(genera_texto_item(i, descripcion, cantidad, precio))

    item.setSizeHint(itemWidget.sizeHint())
    listWidget.setItemWidget(item, itemWidget)

  listWidget.show()
  app.exec_()

