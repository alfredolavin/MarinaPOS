from peewee import *

database = SqliteDatabase('../marinapos.db')

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class CategoriaFarmacologica(BaseModel):
    nombre = TextField()

    class Meta:
        table_name = 'categoria_farmacologica'

class Cliente(BaseModel):
    apodo = TextField(null=True)
    comentarios = TextField(null=True)
    nombre = TextField()
    rut = TextField(null=True)

    class Meta:
        table_name = 'cliente'

class DetalleProducto(BaseModel):
    nombre = TextField()

    class Meta:
        table_name = 'detalle_producto'

class DetalleCodigoBarras(BaseModel):
    detalle_producto = ForeignKeyField(column_name='detalle_producto_id', field='id', model=DetalleProducto)
    valor = TextField()

    class Meta:
        table_name = 'detalle_codigo_barras'

class PrincipioActivo(BaseModel):
    nombre = TextField()

    class Meta:
        table_name = 'principio_activo'

class TipoReceta(BaseModel):
    nombre = TextField()

    class Meta:
        table_name = 'tipo_receta'

class UnidadMedida(BaseModel):
    nombre = TextField()

    class Meta:
        table_name = 'unidad_medida'

class FormaFarmaceutica(BaseModel):
    nombre = TextField(null=True)
    unidad_de_medida = ForeignKeyField(column_name='unidad_de_medida_id', field='id', model=UnidadMedida)

    class Meta:
        table_name = 'forma_farmaceutica'

class Laboratorio(BaseModel):
    nombre = TextField(unique=True)

    class Meta:
        table_name = 'laboratorio'

class Producto(BaseModel):
    cantidad_por_envase = IntegerField(null=True)
    categoria_farmacologica = ForeignKeyField(column_name='categoria_farmacologica_id', field='id', model=CategoriaFarmacologica, null=True)
    es_bioequivalente = BooleanField(null=True)
    es_cenabast = BooleanField(null=True)
    es_controlado = BooleanField(null=True)
    es_generico = BooleanField(null=True)
    es_refrigerado = BooleanField(null=True)
    forma_farmaceutica = ForeignKeyField(column_name='forma_farmaceutica_id', field='id', model=FormaFarmaceutica, null=True)
    laboratorio = ForeignKeyField(column_name='laboratorio_id', field='id', model=Laboratorio, null=True)
    nombre = TextField()
    pharmid = TextField(null=True)
    principio_activo = ForeignKeyField(column_name='principio_activo_id', field='id', model=PrincipioActivo, null=True)
    registro_isp = TextField(null=True)
    tipo_receta = ForeignKeyField(column_name='tipo_receta_id', field='id', model=TipoReceta, null=True)

    class Meta:
        table_name = 'producto'

class CodigoDeBarras(BaseModel):
    detalle_codigo_barras = ForeignKeyField(column_name='detalle_codigo_barras_id', field='id', model=DetalleCodigoBarras)
    id = TextField(primary_key=True)
    producto = ForeignKeyField(column_name='producto_id', field='id', model=Producto)

    class Meta:
        table_name = 'codigo_de_barras'

class Usuario(BaseModel):
    apodo = TextField()
    nombre = TextField()
    rut = TextField()

    class Meta:
        table_name = 'usuario'

class Turno(BaseModel):
    comentario = TextField(null=True)
    monto_caja_final = IntegerField(null=True)
    monto_caja_final_real = IntegerField(null=True)
    monto_caja_inicial = IntegerField()
    primer_movimiento = DateTimeField(constraints=[SQL("DEFAULT datetime('now','localtime')")])
    ultimo_movimiento = DateTimeField(null=True)
    usuario = ForeignKeyField(column_name='usuario_id', field='id', model=Usuario)

    class Meta:
        table_name = 'turno'

class EstadoDocumento(BaseModel):
    nombre = TextField()

    class Meta:
        table_name = 'estado_documento'

class TipoDocumento(BaseModel):
    nombre = TextField()

    class Meta:
        table_name = 'tipo_documento'

class Documento(BaseModel):
    cliente = ForeignKeyField(column_name='cliente_id', field='id', model=Cliente)
    comentario = TextField(null=True)
    estado_documento = ForeignKeyField(column_name='estado_documento_id', field='id', model=EstadoDocumento)
    momento = DateTimeField(constraints=[SQL("DEFAULT datetime('now','localtime')")])
    tipo_documento = ForeignKeyField(column_name='tipo_documento_id', field='id', model=TipoDocumento)
    total_documento = IntegerField()
    turno = ForeignKeyField(column_name='turno_id', field='id', model=Turno)

    class Meta:
        table_name = 'documento'

class EstadoMovimiento(BaseModel):
    nombre = TextField(unique=True)

    class Meta:
        table_name = 'estado_movimiento'

class TipoMovimiento(BaseModel):
    nombre = TextField(null=True)

    class Meta:
        table_name = 'tipo_movimiento'

class Movimiento(BaseModel):
    documento = ForeignKeyField(column_name='documento_id', field='id', model=Documento)
    es_salida = BooleanField()
    estado_movimiento = ForeignKeyField(column_name='estado_movimiento_id', field='id', model=EstadoMovimiento)
    momento = DateTimeField(constraints=[SQL("DEFAULT datetime('now','localtime')")])
    multiplicador = IntegerField()
    precio_cobrado = IntegerField()
    producto_costo = IntegerField()
    producto = ForeignKeyField(column_name='producto_id', field='id', model=Producto)
    producto_nombre = TextField()
    producto_precio = IntegerField()
    tipo_movimiento = ForeignKeyField(column_name='tipo_movimiento_id', field='id', model=TipoMovimiento)
    turno = ForeignKeyField(column_name='turno_id', field='id', model=Turno)
    ultimo_precio = IntegerField()

    class Meta:
        table_name = 'movimiento'

class TipoPago(BaseModel):
    nombre = TextField()

    class Meta:
        table_name = 'tipo_pago'

class Pago(BaseModel):
    documento = ForeignKeyField(column_name='documento_id', field='id', model=Documento)
    monto = IntegerField()
    tipo_pago = ForeignKeyField(column_name='tipo_pago_id', field='id', model=TipoPago)
    turno = ForeignKeyField(column_name='turno_id', field='id', model=Turno)

    class Meta:
        table_name = 'pago'

class ProductoPrecio(BaseModel):
    momento = DateTimeField(constraints=[SQL("DEFAULT datetime('now','localtime')")])
    precio_compra = IntegerField(null=True)
    precio_venta = IntegerField()
    producto = ForeignKeyField(column_name='producto_id', field='id', model=Producto)
    turno = ForeignKeyField(column_name='turno_id', field='id', model=Turno)

    class Meta:
        table_name = 'producto_precio'

class SqliteSequence(BaseModel):
    name = BareField(null=True)
    seq = BareField(null=True)

    class Meta:
        table_name = 'sqlite_sequence'
        primary_key = False

