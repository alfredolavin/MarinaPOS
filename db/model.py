from peewee import *

database = SqliteDatabase('marinapos.db')

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class UnidadDeMedida(BaseModel):
    nombre = TextField(null=True, unique=True)

    class Meta:
        table_name = 'unidad_de_medida'

class FormaFarmaceutica(BaseModel):
    nombre = TextField(null=True, unique=True)
    unidad_de_medida = ForeignKeyField(column_name='unidad_de_medida_id', field='id', model=UnidadDeMedida)

    class Meta:
        table_name = 'forma_farmaceutica'

class Laboratorio(BaseModel):
    nombre = TextField(null=True, unique=True)

    class Meta:
        table_name = 'laboratorio'

class Producto(BaseModel):
    cantidad = IntegerField(null=True)
    concentracion = TextField(null=True)
    costo = IntegerField()
    es_activo = BooleanField(null=True)
    es_bioequivalente = BooleanField(null=True)
    es_controlado = BooleanField(null=True)
    es_generico = BooleanField(null=True)
    es_petitorio_minimo = BooleanField(null=True)
    es_refrigerado = BooleanField(null=True)
    forma_farmaceutica = ForeignKeyField(column_name='forma_farmaceutica_id', field='id', model=FormaFarmaceutica)
    laboratorio = ForeignKeyField(column_name='laboratorio_id', field='id', model=Laboratorio)
    nombre = TextField(index=True)
    precio = IntegerField()
    principio_activo = TextField(index=True, null=True)
    registro_isp = TextField(null=True)
    stock = IntegerField(null=True)
    unidad_de_concentracion = ForeignKeyField(column_name='unidad_de_concentracion_id', field='id', model=UnidadDeMedida)

    class Meta:
        table_name = 'producto'

class CodigoDeBarras(BaseModel):
    barras = TextField(unique=True)
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

class SqliteSequence(BaseModel):
    name = BareField(null=True)
    seq = BareField(null=True)

    class Meta:
        table_name = 'sqlite_sequence'
        primary_key = False

