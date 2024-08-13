'Escanée su código para abrir turno'
'Ingrese monto inicial caja', 'Ej: $50.000'
'Ingrese productos venta #16', 'Ej: 78481184181224'
'Vuelva a presionar enter para finalizar la venta'
'Ingrese nuevo precio temporal para %S', 'Ej: $9.900'
'Cambiar precio de % a:', 'Ej: $9.900', 'Precio muy bajo, debe ser mayor'
'Ingrese monto final caja', 'Monto invalido, vuelva a intentar'
'Ingrese comentarios turno', 'Se compraron lápices'
'Ingrese nombre para guardar venta:'


'Ingrese 1) Proveedor'
'Ingrese 2) Tipo Documento'
'Ingrese 3) Número Documento'
'Ingrese 4) Proveedor'

'Crear nueva opción %?'
'Escriba SI para crear nueva opción':'Ej: SI'

'/VENDER'
'/CERRAR TURNO'
'/CREAR PRODUCTO'
'/CREAR LABORATORIO O MARCA'
'/CAMBIAR DE USUARIO'

MAQUINA DE ESTADO:
  ESTADO 0:

    VENTA: Presione Enter 3 vecesseguidas para finalizar la venta, Presione Enter dos veces para agregar de nuevo el último producto. Presione escape 1 vez para deshacer la ultima acción. Ponga un signo menos - y luego enter para eliminar el último producto, o unsigno menos y escanée el código a eliminar, o un signo menos y el número de línea que desea borrar. Presiones Esc tres veces para borrar todos los productos
    * '/BORRAR TODO'
      '/CARGAR VENTA GUARDADA'
      '/GUARDAR VENTA'
      '/CAMBIAR DE USUARIO'
      '/CERRAR TURNO'
      '/REALIZAR RETIRO'
      '/IMPRIMIR COMO COTIZACION'
    INGRESO_FACTURA:

