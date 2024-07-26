# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class lista_nombres(models.Model):
  nombre = models.TextField(unique=True, blank=False, null=False)

  def __str__(self):
    return self.nombre

  class Meta:
    abstract = True


class CategoriaFarmacologica(lista_nombres):

  class Meta:
    db_table = "categoria_farmacologica"


class Cliente(lista_nombres):
  rut = models.TextField(blank=True, null=True)
  apodo = models.TextField(blank=True, null=True)
  comentarios = models.TextField(blank=True, null=True)

  class Meta:
    db_table = "cliente"


class CodigoDeBarras(models.Model):
  id = models.TextField(primary_key=True)
  producto = models.ForeignKey("Producto", models.DO_NOTHING)
  detalle_codigo_barras = models.ForeignKey(
      "DetalleCodigoBarras", models.DO_NOTHING)

  class Meta:
    db_table = "codigo_de_barras"


class DetalleCodigoBarras(models.Model):
  detalle_producto = models.ForeignKey("DetalleProducto", models.DO_NOTHING)
  valor = models.TextField()

  class Meta:
    db_table = "detalle_codigo_barras"


class DetalleProducto(lista_nombres):

  class Meta:
    db_table = "detalle_producto"


class Documento(models.Model):
  tipo_documento = models.ForeignKey("TipoDocumento", models.DO_NOTHING)
  estado_documento = models.ForeignKey("EstadoDocumento", models.DO_NOTHING)
  cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
  momento = models.DateTimeField()
  total_documento = models.IntegerField()
  comentario = models.TextField(blank=True, null=True)
  turno = models.ForeignKey("Turno", models.DO_NOTHING)

  class Meta:
    db_table = "documento"


class EstadoDocumento(lista_nombres):

  class Meta:
    db_table = "estado_documento"


class EstadoMovimiento(lista_nombres):

  class Meta:
    db_table = "estado_movimiento"


class FormaFarmaceutica(lista_nombres):
  unidad_de_medida = models.ForeignKey("UnidadMedida", models.DO_NOTHING)

  class Meta:
    db_table = "forma_farmaceutica"


class Laboratorio(lista_nombres):

  class Meta:
    db_table = "laboratorio"


class Movimiento(models.Model):
  producto = models.ForeignKey("Producto", models.DO_NOTHING)
  estado_movimiento = models.ForeignKey(EstadoMovimiento, models.DO_NOTHING)
  tipo_movimiento = models.ForeignKey("TipoMovimiento", models.DO_NOTHING)
  documento = models.ForeignKey(Documento, models.DO_NOTHING)
  turno = models.ForeignKey("Turno", models.DO_NOTHING)
  momento = models.DateTimeField()
  producto_nombre = models.TextField()
  producto_precio = models.IntegerField()
  producto_costo = models.IntegerField()
  precio_cobrado = models.IntegerField()
  multiplicador = models.IntegerField()
  ultimo_precio = models.IntegerField()
  es_salida = models.BooleanField()

  class Meta:
    db_table = "movimiento"


class Pago(models.Model):
  tipo_pago = models.ForeignKey("TipoPago", models.DO_NOTHING)
  turno = models.ForeignKey("Turno", models.DO_NOTHING)
  documento = models.ForeignKey(Documento, models.DO_NOTHING)
  monto = models.IntegerField()

  class Meta:
    db_table = "pago"


class PrincipioActivo(lista_nombres):

  class Meta:
    db_table = "principio_activo"


class Producto(lista_nombres):
  pharmid = models.TextField(blank=True, null=True)
  laboratorio = models.ForeignKey(
      Laboratorio, models.DO_NOTHING, blank=True, null=True
  )
  categoria_farmacologica = models.ForeignKey(
      CategoriaFarmacologica, models.DO_NOTHING, blank=True, null=True
  )
  forma_farmaceutica = models.ForeignKey(
      FormaFarmaceutica, models.DO_NOTHING, blank=True, null=True
  )
  principio_activo = models.ForeignKey(
      PrincipioActivo, models.DO_NOTHING, blank=True, null=True
  )
  tipo_receta = models.ForeignKey(
      "TipoReceta", models.DO_NOTHING, blank=True, null=True
  )
  registro_isp = models.TextField(blank=True, null=True)
  es_cenabast = models.BooleanField(blank=True, null=True)
  es_controlado = models.BooleanField(blank=True, null=True)
  es_refrigerado = models.BooleanField(blank=True, null=True)
  es_bioequivalente = models.BooleanField(blank=True, null=True)
  es_generico = models.BooleanField(blank=True, null=True)
  cantidad_por_envase = models.IntegerField(blank=True, null=True)

  class Meta:
    db_table = "producto"


class ProductoPrecio(models.Model):
  producto = models.ForeignKey(Producto, models.DO_NOTHING)
  momento = models.DateTimeField()
  precio_venta = models.IntegerField()
  precio_compra = models.IntegerField(blank=True, null=True)
  turno = models.ForeignKey("Turno", models.DO_NOTHING)

  class Meta:
    db_table = "producto_precio"


class TipoDocumento(lista_nombres):

  class Meta:
    db_table = "tipo_documento"


class TipoMovimiento(lista_nombres):

  class Meta:
    db_table = "tipo_movimiento"


class TipoPago(lista_nombres):

  class Meta:
    db_table = "tipo_pago"


class TipoReceta(lista_nombres):

  class Meta:
    db_table = "tipo_receta"


class Turno(models.Model):
  usuario = models.ForeignKey("Usuario", models.DO_NOTHING)
  primer_movimiento = models.DateTimeField()
  monto_caja_inicial = models.IntegerField()
  ultimo_movimiento = models.DateTimeField(blank=True, null=True)
  monto_caja_final = models.IntegerField(blank=True, null=True)
  monto_caja_final_real = models.IntegerField(blank=True, null=True)
  comentario = models.TextField(blank=True, null=True)

  class Meta:
    db_table = "turno"


class UnidadMedida(lista_nombres):

  class Meta:
    db_table = "unidad_medida"


class Usuario(lista_nombres):
  rut = models.TextField()
  apodo = models.TextField()

  class Meta:
    db_table = "usuario"
