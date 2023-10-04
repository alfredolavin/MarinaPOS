from peewee import *

database = SqliteDatabase('../marinapos.db')

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class CodigoAtc(BaseModel):
    descripcion = TextField()
    nombre = TextField()

    class Meta:
        table_name = 'codigo_atc'

class UnidadDeMedida(BaseModel):
    descripcion = TextField()
    nombre = TextField(unique=True)
    unidad_de_medida_id = AutoField()

    class Meta:
        table_name = 'unidad_de_medida'

class FormaFarmaceutica(BaseModel):
    nombre = TextField(null=True, unique=True)
    unidad_de_medida = ForeignKeyField(column_name='unidad_de_medida_id', field='unidad_de_medida_id', model=UnidadDeMedida)

    class Meta:
        table_name = 'forma_farmaceutica'

class Laboratorio(BaseModel):
    nombre = TextField(null=True, unique=True)

    class Meta:
        table_name = 'laboratorio'

class Producto(BaseModel):
    cantidad = IntegerField()
    concentracion = TextField()
    es_activo = BooleanField(null=True)
    es_bioequivalente = BooleanField(null=True)
    es_controlado = BooleanField(null=True)
    es_generico = BooleanField(null=True)
    es_petitorio_minimo = BooleanField(null=True)
    es_refrigerado = BooleanField(null=True)
    forma_farmaceutica = ForeignKeyField(column_name='forma_farmaceutica_id', field='id', model=FormaFarmaceutica)
    laboratorio = ForeignKeyField(column_name='laboratorio_id', field='id', model=Laboratorio)
    nombre = TextField()
    nombre_largo = TextField(index=True)
    unidad_de_cantidad = ForeignKeyField(column_name='unidad_de_cantidad', field='unidad_de_medida_id', model=UnidadDeMedida)
    unidad_de_concentracion = ForeignKeyField(backref='unidad_de_medida_unidad_de_concentracion_set', column_name='unidad_de_concentracion', field='unidad_de_medida_id', model=UnidadDeMedida)

    class Meta:
        table_name = 'producto'

class CodigoDeBarras(BaseModel):
    barras = TextField(unique=True)
    producto = ForeignKeyField(column_name='producto_id', field='id', model=Producto)

    class Meta:
        table_name = 'codigo_de_barras'

class TipoDetalle(BaseModel):
    nombre_detalle = TextField()

    class Meta:
        table_name = 'tipo_detalle'

class DetalleProducto(BaseModel):
    detalle = TextField()
    producto = ForeignKeyField(column_name='producto_id', field='id', model=Producto)
    tipo_detalles = ForeignKeyField(column_name='tipo_detalles_id', field='id', model=TipoDetalle)

    class Meta:
        table_name = 'detalle_producto'
        indexes = (
            (('producto', 'tipo_detalles'), True),
            (('producto', 'tipo_detalles'), True),
        )
        primary_key = CompositeKey('producto', 'tipo_detalles')

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
    primer_movimiento = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    ultimo_movimiento = DateTimeField(null=True)
    usuario = ForeignKeyField(column_name='usuario_id', field='id', model=Usuario)

    class Meta:
        table_name = 'turno'

class EstadoDocumento(BaseModel):
    nombre = TextField(null=True, unique=True)

    class Meta:
        table_name = 'estado_documento'

class TipoDocumento(BaseModel):
    nombre = TextField(null=True, unique=True)

    class Meta:
        table_name = 'tipo_documento'

class Documento(BaseModel):
    comentario = TextField(null=True)
    estado_documento = ForeignKeyField(column_name='estado_documento_id', field='id', model=EstadoDocumento)
    momento = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    tipo_documento = ForeignKeyField(column_name='tipo_documento_id', field='id', model=TipoDocumento)
    total_documento = IntegerField()
    turno = ForeignKeyField(column_name='turno_id', field='id', model=Turno)

    class Meta:
        table_name = 'documento'

class EstadoMovimiento(BaseModel):
    nombre = TextField(null=True, unique=True)

    class Meta:
        table_name = 'estado_movimiento'

class Movimiento(BaseModel):
    documento = ForeignKeyField(column_name='documento_id', field='id', model=Documento)
    estado_movimiento = ForeignKeyField(column_name='estado_movimiento_id', field='id', model=EstadoMovimiento)
    multiplicador = IntegerField()
    precio_cobrado = IntegerField()
    producto_costo = IntegerField()
    producto = ForeignKeyField(column_name='producto_id', field='id', model=Producto)
    producto_nombre = TextField()
    producto_precio = IntegerField()

    class Meta:
        table_name = 'movimiento'

class PrincipioActivo(BaseModel):
    nombre = TextField()

    class Meta:
        table_name = 'principio_activo'

class PrincipioActivoYCodigoAtc(BaseModel):
    codigo_atc = ForeignKeyField(column_name='codigo_atc_id', field='id', model=CodigoAtc)
    principio_activo = ForeignKeyField(column_name='principio_activo_id', field='id', model=PrincipioActivo)

    class Meta:
        table_name = 'principio_activo_y_codigo_atc'
        indexes = (
            (('codigo_atc', 'principio_activo'), True),
        )
        primary_key = CompositeKey('codigo_atc', 'principio_activo')

class PrincipioActivoYProducto(BaseModel):
    concentracion = IntegerField()
    principio_activo = ForeignKeyField(column_name='principio_activo_id', field='id', model=PrincipioActivo)
    producto = ForeignKeyField(column_name='producto_id', field='id', model=Producto)
    unidad_de_medida = ForeignKeyField(column_name='unidad_de_medida_id', field='unidad_de_medida_id', model=UnidadDeMedida)

    class Meta:
        table_name = 'principio_activo_y_producto'
        indexes = (
            (('producto', 'principio_activo'), True),
        )
        primary_key = CompositeKey('principio_activo', 'producto')

class ProductoPrecio(BaseModel):
    momento = DateTimeField()
    precio_compra = IntegerField(null=True)
    precio_venta = IntegerField()
    producto = ForeignKeyField(column_name='producto_id', field='id', model=Producto)
    usuario = ForeignKeyField(column_name='usuario_id', field='id', model=Usuario)

    class Meta:
        table_name = 'producto_precio'

class SqliteSequence(BaseModel):
    name = BareField(null=True)
    seq = BareField(null=True)

    class Meta:
        table_name = 'sqlite_sequence'
        primary_key = False

class TipoPago(BaseModel):
    _1 = TextField(column_name='1', null=True)
    efectivo = TextField(column_name='EFECTIVO', null=True)

    class Meta:
        table_name = 'tipo_pago'
        primary_key = False

class TipoReceta(BaseModel):
    _450000001 = TextField(column_name='450000001', null=True)
    libre = TextField(column_name='LIBRE', null=True)

    class Meta:
        table_name = 'tipo_receta'
        primary_key = False

