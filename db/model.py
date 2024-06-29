from peewee import *

database = SqliteDatabase('../marinapos.db')

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Base(BaseModel):
    __4 = TextField(column_name='?_4', null=True)
    __5 = TextField(column_name='?_5', null=True)
    bioequivalent = TextField(column_name='BIOEQUIVALENT', null=True)
    brand = TextField(column_name='BRAND', null=True)
    cenabast = TextField(column_name='CENABAST', null=True)
    code_isp = TextField(column_name='CODE_ISP', null=True)
    concentration = TextField(column_name='CONCENTRATION', null=True)
    cooled = TextField(column_name='COOLED', null=True)
    ean13 = TextField(column_name='EAN13', null=True)
    editable_name = TextField(column_name='EDITABLE_NAME', null=True)
    farmid = TextField(column_name='FARMID', null=True)
    laboratory = TextField(column_name='LABORATORY', null=True)
    laboratory_id = TextField(column_name='LABORATORY_ID', null=True)
    liquid = TextField(column_name='LIQUID', null=True)
    prescription_type = TextField(column_name='PRESCRIPTION_TYPE', null=True)
    prescription_type_id = TextField(column_name='PRESCRIPTION_TYPE_ID', null=True)
    principe_active = TextField(column_name='PRINCIPE_ACTIVE', null=True)
    principe_active_id = TextField(column_name='PRINCIPE_ACTIVE_ID', null=True)
    quantity_per_container = TextField(column_name='QUANTITY_PER_CONTAINER', null=True)
    select = TextField(column_name='SELECT', null=True)
    shape_pharmacy = TextField(column_name='SHAPE_PHARMACY', null=True)
    shape_pharmacy2 = TextField(column_name='SHAPE_PHARMACY2', null=True)
    shape_pharmacy2_id = TextField(column_name='SHAPE_PHARMACY2_id', null=True)
    sub_category = TextField(column_name='SUB_CATEGORY', null=True)
    sub_category_id = TextField(column_name='SUB_CATEGORY_ID', null=True)
    unidad = TextField(column_name='UNIDAD', null=True)
    unidad_id = TextField(column_name='UNIDAD_ID', null=True)
    producto_id = TextField(null=True)

    class Meta:
        table_name = 'BASE'
        primary_key = False

class CategoriaFarmacologica(BaseModel):
    nombre = TextField(null=True, unique=True)

    class Meta:
        table_name = 'categoria_farmacologica'

class PrincipioActivo(BaseModel):
    nombre = TextField()

    class Meta:
        table_name = 'principio_activo'

class TipoReceta(BaseModel):
    nombre = TextField()

    class Meta:
        table_name = 'tipo_receta'

class UnidadMedida(BaseModel):
    nombre = TextField(unique=True)

    class Meta:
        table_name = 'unidad_medida'

class FormaFarmaceutica(BaseModel):
    nombre = TextField(null=True, unique=True)
    unidad_de_medida = ForeignKeyField(column_name='unidad_de_medida_id', field='id', model=UnidadMedida)

    class Meta:
        table_name = 'forma_farmaceutica'

class Laboratorio(BaseModel):
    nombre = TextField(null=True, unique=True)

    class Meta:
        table_name = 'laboratorio'

class Producto(BaseModel):
    cantidad_por_envase = IntegerField(null=True)
    categoria_farmacologica = ForeignKeyField(column_name='categoria_farmacologica_id', field='id', model=CategoriaFarmacologica)
    es_bioequivalente = BooleanField(null=True)
    es_cenabast = BooleanField(null=True)
    es_controlado = BooleanField(null=True)
    es_generico = BooleanField(null=True)
    es_refrigerado = BooleanField(null=True)
    forma_farmaceutica = ForeignKeyField(column_name='forma_farmaceutica_id', field='id', model=FormaFarmaceutica)
    laboratorio = ForeignKeyField(column_name='laboratorio_id', field='id', model=Laboratorio)
    nombre = TextField()
    principio_activo = ForeignKeyField(column_name='principio_activo_id', field='id', model=PrincipioActivo)
    registro_isp = TextField(null=True)
    tipo_receta = ForeignKeyField(column_name='tipo_receta_id', field='id', model=TipoReceta)

    class Meta:
        table_name = 'producto'

class CodigoDeBarras(BaseModel):
    id = TextField(primary_key=True)
    producto = ForeignKeyField(column_name='producto_id', field='id', model=Producto)

    class Meta:
        table_name = 'codigo_de_barras'

class CodigosFisicos(BaseModel):
    _16400 = TextField(column_name='16400', null=True)
    _7795373013773 = TextField(column_name='7795373013773', null=True)
    fusimed_b_emul_top_15_g_ = TextField(column_name='FUSIMED-B EMUL.TOP.15 G. ', null=True)

    class Meta:
        table_name = 'codigos_fisicos'
        primary_key = False

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
    turno = ForeignKeyField(column_name='turno_id', field='id', model=Turno)

    class Meta:
        table_name = 'movimiento'

class TipoPago(BaseModel):
    nombre = TextField()

    class Meta:
        table_name = 'tipo_pago'

class Pago(BaseModel):
    documento = ForeignKeyField(column_name='documento_id', field='id', model=Documento)
    monto = IntegerField(null=True)
    tipo_pago = ForeignKeyField(column_name='tipo_pago_id', field='id', model=TipoPago)
    turno = ForeignKeyField(column_name='turno_id', field='id', model=Turno)

    class Meta:
        table_name = 'pago'

class ProductoPrecio(BaseModel):
    momento = DateTimeField()
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

